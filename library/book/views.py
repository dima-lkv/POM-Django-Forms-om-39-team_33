from django.shortcuts import render


def showBooks(request):
    return render(request, 'book/book.html')
