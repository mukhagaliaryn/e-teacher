from django.shortcuts import render, get_object_or_404
from .models import Book, Genre


def book_list(request):
    genres = Genre.objects.all()
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books, 'genres': genres})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.view += 1
    book.save()
    return render(request, 'books/detail.html', {'book': book, })
