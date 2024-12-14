from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import Category, Subject
from progress.models import UserSubject


# Main view
def main(request):
    return render(request, 'index.html', {})


# Home view
@login_required(login_url='/accounts/login/')
def home(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject = get_object_or_404(Subject, id=subject_id)

        if not subject_id or not subject_id.isdigit():
            messages.error(request, 'Қате сұрау: элемент идентификаторы жоқ.')
            return redirect('home')

        if UserSubject.objects.filter(user=request.user, subject=subject).exists():
            messages.error(request, 'Сіз бұл пәнді қосып қойғансыз.')
        else:
            UserSubject.objects.create(user=request.user, subject=subject)
            messages.success(request, f'"{subject.title}" пәні қосылды!')
        return redirect('home')

    access_subjects = request.user.access_subjects.all()
    my_subjects = UserSubject.objects.filter(user=request.user)
    add_subjects = [user_subject.subject for user_subject in my_subjects]

    context = {
        'access_subjects': access_subjects,
        'my_subjects': my_subjects,
        'add_subjects': add_subjects
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
    return render(request, 'home/subjects.html', context)


# Subject detail view
@login_required(login_url='/accounts/login/')
def subject_detail(request, subject_pk):
    subject = get_object_or_404(Subject, pk=subject_pk)
    my_subjects = request.user.user_subjects.all()
    add_subjects = [user_subject.subject for user_subject in my_subjects]
    context = {
        'subject': subject,
        'add_subjects': add_subjects
    }
    return render(request, 'home/subject_detail.html', context)


# UserCourse detail view
@login_required(login_url='/accounts/login/')
def user_subject_detail(request, user_course_pk):

    context = {
        'user_course_pk': user_course_pk
    }
    return render(request, 'home/user_course_detail.html', context)

