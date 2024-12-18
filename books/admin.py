from django.contrib import admin
from .models import Book, Genre, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    search_fields = ('title', 'description')
    list_filter = ('category', 'authors', 'published_date')
    filter_horizontal = ('authors', )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name',)