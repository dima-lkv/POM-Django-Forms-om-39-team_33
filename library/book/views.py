from django.shortcuts import render
from itertools import chain
from author.models import Author
from .models import Book
from django.contrib.auth.decorators import login_required
from operator import attrgetter


@login_required(login_url='login')
def searchBooks(request):
    query = request.GET.get('query')
    if not query:
        return showBooks(request)
    by_id = None
    try:
        by_id = Book.objects.all().filter(id=int(query))
    except:
        print('no int')
    by_name = Book.objects.all().filter(name__icontains=query)
    by_description = Book.objects.all().filter(description__icontains=query)
    by_author_name = Book.objects.all().filter(authors__name__icontains=query)
    by_author_surname = Book.objects.all().filter(authors__surname__icontains=query)
    if by_id:
        result_list = list(chain(by_id, by_name, by_description, by_author_name, by_author_surname))
    else:
        result_list = list(chain(by_name, by_description, by_author_name, by_author_surname))
    book_author_zip = zip(result_list, get_authors(result_list))
    return render(request, 'book/book.html', {'book_author_zip': book_author_zip})


@login_required(login_url='login')
def showBooks(request):
    books_query = Book.objects.order_by('id')
    book_author_zip = zip(books_query, get_authors(books_query))
    return render(request, 'book/book.html', {'book_author_zip': book_author_zip})


def get_authors(books):
    authors_list = []
    if type(books) == Book:
        print(True)
        book = books
        print(book.authors)
        if list(book.authors.all()):
            for author in book.authors.all():
                authors_list.append(author)
        else:
            authors_list.append(None)
    else:
        for book in books:
            temp = []
            if list(book.authors.all()):
                for author in book.authors.all():
                    temp.append(author)
                authors_list.append(temp)
            else:
                authors_list.append(None)
    return authors_list


def showOrderedBooks(request, pk):
    books_query = Book.objects.order_by(pk)
    book_author_zip = zip(books_query, get_authors(books_query))
    return render(request, 'book/book.html', {'book_author_zip': book_author_zip})


def showSpecificBook(request, id):
    book_obj = Book.objects.get(id=id)
    return render(request, 'book/specificBook.html', {'book': book_obj, 'authors': get_authors(book_obj)})

@login_required(login_url='login')
def createBook(request):
    if request.user.role != 1:
        text = 'You have no permission to view this page'
        return render(request, 'authentication/denied.html', {'text': text})
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        count = request.POST.get('count')
        Book.create(name=name, description=description, count=count)
    return render(request, 'book/create_book.html')

