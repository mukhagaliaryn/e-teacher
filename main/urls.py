from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('subjects/', views.subjects, name='subjects'),
    path('subject/<subject_pk>/', views.subject_detail, name='subject_detail'),
    path('user/subject/<user_course_pk>/', views.user_subject_detail, name='user_subject_detail')
]