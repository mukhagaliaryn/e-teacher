from django.contrib import admin
from .models import UserSubject, UserLesson


@admin.register(UserSubject)
class UserSubjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at')
    list_filter = ('user', 'subject')
    search_fields = ('user__username', 'subject__title')


@admin.register(UserLesson)
class UserLessonAdmin(admin.ModelAdmin):
    list_display = ('user_subject', 'lesson', 'lesson_score', 'completed', 'completed_at')
    list_filter = ('completed', )
    search_fields = ('user_subject__user__username', 'lesson__title')
