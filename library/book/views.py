from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showBooks(request):
    #q = request.GET.get('q') if request.GET.get('q') != None else ''
    #books_query = Book.objects.filter(name__name__icontains=q)
    search_by = request.GET.get('search_by')
    query = request.GET.get('query')
    if search_by == 'name':
        books_query = Book.objects.filter(name=query)
    else:
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
        print(authors_list)
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
