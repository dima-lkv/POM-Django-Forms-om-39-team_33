from django.shortcuts import render
from .models import *


def showAuthors(request):
    authors = Author.objects.all()
    return render(request, 'author/author.html', {'authors': authors})
