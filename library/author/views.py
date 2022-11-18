from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from book.models import Book
from .models import Author


@login_required(login_url='login')
def showAuthors(request):
    if request.user.role != 1:
        text = 'You have no permission to view this page'
        return render(request, 'authentication/denied.html', {'text': text})
    authors = Author.objects.all()
    book_author_zip = zip(get_books(authors), authors)
    return render(request, 'author/author.html', {'book_author_zip': book_author_zip})


def get_books(authors):
    book_list = []
    for author in authors:
        temp = []
        if list(author.books.all()):
            for book in author.books.all():
                temp.append(book)
            book_list.append(temp)
        else:
            book_list.append(None)
    return book_list


@login_required(login_url='login')
def createAuthor(request):
    if request.user.role != 1:
        text = 'You have no permission to view this page'
        return render(request, 'authentication/denied.html', {'text': text})
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        our_author = Author.create(name, surname, patronymic)
        if not request.POST.get('books'):
            messages.error(request, 'No book with such id.')
            return redirect('create_author')
        books = request.POST.get('books')
        books_list = books.split(',')
        for book_id in books_list:
            if Book.get_by_id(book_id):
                Book.get_by_id(book_id).add_authors(authors=[our_author])
    return render(request, 'author/create_author.html')


def removeAuthor(request, id):
    Author.delete_by_id(id)
    return redirect('author')
