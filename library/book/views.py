from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showBooks(request):
    books = Book.objects.all()
    return render(request, 'book/book.html', {'books': books})
