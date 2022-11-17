from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showBooks(request):
    books = Book.objects.all()

    def get_authors(books_query):
        authors = []
        for book in books:
            temp = []
            print('book.authors', list(book.authors.all()))
            if list(book.authors.all()):
                for author in book.authors.all():
                    temp.append(author)
                authors.append(temp)
            else:
                authors.append(None)
        return authors
    authors = get_authors(books)

    book_author_zip = zip(books, authors)
    return render(request, 'book/book.html', {'book_author_zip': book_author_zip})


def showOrderedBooks(request, pk):
    # reversed()
    books = (Book.objects.order_by(pk))
    name = 'Books'
    return render(request, 'book/book.html', {'books': books, 'name': name})


def showSpecificBook(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book/specificBook.html', {'book': book})
