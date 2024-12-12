from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Main view
def main(request):
    return render(request, 'index.html', {})


# Home view
@login_required(login_url='/accounts/login/')
def home(request):
    new_courses = [1, 2, 3]

    context = {
        'new_courses': new_courses
    }
    return render(request, 'home/index.html', context)


# Courses view
@login_required(login_url='/accounts/login/')
def courses(request):
    all_courses = [1, 2, 3, 4, 5]

    context = {
        'courses': all_courses
    }
    return render(request, 'home/courses.html', context)