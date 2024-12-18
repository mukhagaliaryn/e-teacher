from django.contrib import admin
from .models import Category, Subject, Chapter, Lesson, TextContent, VideoContent, Comment, Homework, FrameContent, \
    LessonDocs
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', 'slug', )
    ordering = ('name',)


class ChapterTab(admin.TabularInline):
    model = Chapter
    extra = 1

@admin.register(Subject)
class SubjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'created_at', 'view', )
    list_filter = ('category',)
    search_fields = ('title', 'description')
    filter_horizontal = ('observers', )
    inlines = (ChapterTab, )


class LessonTab(SummernoteModelAdminMixin, admin.StackedInline):
    model = Lesson
    extra = 1

@admin.register(Chapter)
class ChapterAdmin(SummernoteModelAdmin):
    list_display = ('title', 'subject', 'order')
    list_filter = ('subject',)
    ordering = ('order',)
    inlines = (LessonTab, )


class TextContentTab(SummernoteModelAdminMixin, admin.TabularInline):
    model = TextContent
    extra = 1

class VideoContentTab(admin.TabularInline):
    model = VideoContent
    extra = 1

class FrameContentTab(admin.TabularInline):
    model = FrameContent
    extra = 1


class FileDocTab(admin.TabularInline):
    model = LessonDocs
    extra = 1


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin):
    list_display = ('title', 'chapter', 'order')
    list_filter = ('subject', 'chapter',)
    ordering = ('chapter', 'order')
    inlines = (VideoContentTab, TextContentTab, FrameContentTab, FileDocTab, )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'author', 'created_at', 'content')
    search_fields = ('author', 'content')
    list_filter = ('lesson', 'created_at')


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'student', 'submitted_at', 'grade')
    search_fields = ('student',)
    list_filter = ('lesson', 'submitted_at')
    ordering = ('-submitted_at',)
