from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    print(request.path)
    return render(request, 'author/create_author.html')


def removeAuthor(request):
    author_id = request.POST.get('author_id')
    Author.delete_by_id(author_id)
    return redirect('author')
