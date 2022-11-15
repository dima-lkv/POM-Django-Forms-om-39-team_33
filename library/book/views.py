from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showBooks(request):
    books = Book.objects.all()
    return render(request, 'book/book.html', {'books': books})


def showOrderedBooks(request, pk):
    # reversed()
    books = (Book.objects.order_by(pk))
    return render(request, 'book/book.html', {'books': books})


def showSpecificBook(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, 'book/', {'book': book})
