from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import Category, Subject, Lesson, Chapter
from progress.models import UserSubject, UserLesson, Homework, Comment, UserHomework


# Main view
def main(request):
    return render(request, 'index.html', {})


# Home view
@login_required(login_url='/accounts/login/')
def home(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        if not subject_id or not subject_id.isdigit():
            messages.error(request, 'Қате сұрау: элемент идентификаторы жоқ.')
            return redirect('home')

        subject = get_object_or_404(Subject, id=subject_id)
        has_lessons = Lesson.objects.filter(chapter__subject=subject).exists()
        if not has_lessons:
            messages.error(request, f'"{subject.title}" пәнінде сабақтар жоқ, оны қосу мүмкін емес.')
            return redirect('home')

        if UserSubject.objects.filter(user=request.user, subject=subject).exists():
            messages.error(request, 'Сіз бұл пәнді қосып қойғансыз.')
        else:
            user_subject = UserSubject.objects.create(user=request.user, subject=subject)
            messages.success(request, f'"{subject.title}" пәні қосылды!')
            lessons = Lesson.objects.filter(chapter__subject=subject)
            user_lessons = [
                UserLesson(user_subject=user_subject, lesson=lesson, completed=False)
                for lesson in lessons
            ]
            UserLesson.objects.bulk_create(user_lessons)
            messages.success(request, f'"{subject.title}" пәнінің сабақтары қосылды!')

        return redirect('home')

    access_subjects = request.user.access_subjects.all()
    my_subjects = UserSubject.objects.filter(user=request.user)
    add_subjects = [user_subject.subject for user_subject in my_subjects]
    first_lesson_ids = {}

    for user_subject in my_subjects:
        lesson = Lesson.objects.filter(chapter__subject=user_subject.subject).order_by('order').first()

        if lesson:
            user_lesson, created = UserLesson.objects.get_or_create(
                user_subject=user_subject,
                lesson=lesson,
            )
            first_lesson_ids[user_subject.id] = user_lesson.id

    context = {
        'access_subjects': access_subjects,
        'my_subjects': my_subjects,
        'add_subjects': add_subjects,
        'first_lesson_ids': first_lesson_ids
    }
    return render(request, 'home/index.html', context)


# Subjects view
@login_required(login_url='/accounts/login/')
def subjects(request):
    categories = Category.objects.all()
    my_subjects = request.user.user_subjects.all()
    add_subjects = [user_subject.subject for user_subject in my_subjects]

    context = {
        'categories': categories,
        'access_subjects': my_subjects,
        'add_subjects': add_subjects
    }
    return render(request, 'subjects/index.html', context)


# Subject detail view
@login_required(login_url='/accounts/login/')
def subject_detail(request, subject_pk):
    subject = get_object_or_404(Subject, pk=subject_pk)
    subject.view += 1
    subject.save()

    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        if not subject_id or not subject_id.isdigit():
            messages.error(request, 'Қате сұрау: элемент идентификаторы жоқ.')
            return redirect('subject_detail', subject_pk=subject.id)

        has_lessons = Lesson.objects.filter(chapter__subject=subject).exists()
        if not has_lessons:
            messages.error(request, f'"{subject.title}" пәнінде сабақтар жоқ, оны қосу мүмкін емес.')
            return redirect('subject_detail', subject_pk=subject.id)

        if UserSubject.objects.filter(user=request.user, subject=subject).exists():
            messages.error(request, 'Сіз бұл пәнді қосып қойғансыз.')
        else:
            user_subject = UserSubject.objects.create(user=request.user, subject=subject)
            messages.success(request, f'"{subject.title}" пәні қосылды!')
            lessons = Lesson.objects.filter(chapter__subject=subject)
            user_lessons = [
                UserLesson(user_subject=user_subject, lesson=lesson, completed=False)
                for lesson in lessons
            ]
            UserLesson.objects.bulk_create(user_lessons)
            messages.success(request, f'"{subject.title}" пәнінің сабақтары қосылды!')

        return redirect('subject_detail', subject_pk=subject.id)

    first_user_subject = UserSubject.objects.filter(user=request.user, subject=subject).order_by('id').first()

    first_user_lesson = None
    if first_user_subject:
        first_user_lesson = UserLesson.objects.filter(
            user_subject=first_user_subject
        ).order_by('lesson__order').first()

    my_subjects = request.user.user_subjects.all()
    add_subjects = [user_subject.subject for user_subject in my_subjects]
    context = {
        'subject': subject,
        'add_subjects': add_subjects,
        'first_user_subject': first_user_subject,
        'first_user_lesson': first_user_lesson
    }
    return render(request, 'subjects/detail.html', context)


# UserCourse detail view
@login_required(login_url='/accounts/login/')
def lesson_detail(request, user_subject_pk, user_lesson_pk):
    user_subject = get_object_or_404(UserSubject, pk=user_subject_pk, user=request.user)
    user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk, user_subject=user_subject)
    chapters = Chapter.objects.filter(subject=user_subject.subject).order_by('order')
    comments = Comment.objects.filter(lesson=user_lesson.lesson).order_by('created_at')
    send_homeworks = [user_homework.homework for user_homework in request.user.homeworks.all()]

    if request.method == 'POST':
        action = request.POST.get('action')
        content = request.POST.get('content')
        rating = request.POST.get('score')
        homework_id = request.POST.get('homework_id')
        homework = Homework.objects.filter(id=homework_id, lesson=user_lesson.lesson).first()

        if action == 'submit_comment':
            if not content:
                messages.error(request, 'Пікір мәтіні бос болмауы керек!')
            elif not rating or not rating.isdigit() or int(rating) not in range(1, 6):
                messages.error(request, 'Баға 1-ден 5-ке дейін болуы керек!')
            else:
                Comment.objects.create(
                    author=request.user,
                    lesson=user_lesson.lesson,
                    content=content,
                    score=int(rating)
                )
                messages.success(request, 'Пікіріңіз сәтті жіберілді!')
                return redirect('lesson_detail', user_subject_pk=user_subject.pk, user_lesson_pk=user_lesson.pk)

        elif action == 'submit_homework' and homework:
            user_homework_file = request.FILES.get('user_homework_file')
            if user_homework_file:
                data = UserHomework(
                    homework=homework,
                    student=request.user,
                    submission=user_homework_file
                )
                data.save()
                messages.success(request, 'Тапсырма сәтті жіберілді!')
                return redirect('lesson_detail', user_subject_pk=user_subject.pk, user_lesson_pk=user_lesson.pk)

        elif action == 'complete_lesson':
            user_lesson.completed = True
            user_lesson.completed_at = timezone.now()
            if user_lesson.lesson.homeworks.all().count() <= 0:
                user_lesson.lesson_score = 100
            user_lesson.save()
            messages.success(request, 'Сабақ аяқталды!')

    chapters_with_lessons = []
    for chapter in chapters:
        lessons = UserLesson.objects.filter(
            user_subject=user_subject,
            lesson__chapter=chapter
        ).order_by('lesson__order')
        chapters_with_lessons.append({
            'chapter': chapter,
            'user_lessons': lessons
        })

    next_user_lesson = UserLesson.objects.filter(
        user_subject=user_subject,
        lesson__order__gt=user_lesson.lesson.order
    ).order_by('lesson__order').first()

    context = {
        'user_lesson': user_lesson,
        'user_subject': user_subject,
        'chapters_with_lessons': chapters_with_lessons,
        'next_user_lesson': next_user_lesson,
        'comments': comments,
        'send_homeworks': send_homeworks
    }
    return render(request, 'home/lesson_detail.html', context)

