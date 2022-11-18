from django.shortcuts import render
from itertools import chain
from author.models import Author
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showBooks(request):
    #q = request.GET.get('q') if request.GET.get('q') != None else ''
    #books_query = Book.objects.filter(name__name__icontains=q)
    search_by = request.GET.get('search_by')
    query = request.GET.get('query')
    print(search_by)
    print(query)
    if search_by == 'name':
        books_query = Book.objects.all()
        books_needed = books_query.filter(name__contains=query)
    elif search_by == 'author':
        books_query = Book.objects.all()
        books_needed = books_query.filter(authors__name__contains=query)
    else:
        books_needed = Book.objects.order_by('id')
    book_author_zip = zip(books_needed, get_authors(books_needed))
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

