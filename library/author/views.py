from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


@login_required(login_url='login')
def showAuthors(request):
    print(request.path)
    if request.user.role != 1:
        text = 'You have no permission to view this page'
        return render(request, 'authentication/denied.html', {'text': text})
    authors = Author.objects.all()
    return render(request, 'author/author.html', {'authors': authors})


@login_required(login_url='login')
def createAuthor(request):
    if request.user.role != 1:
        text = 'You have no permission to view this page'
        return render(request, 'authentication/denied.html', {'text': text})
    print(request.path)
    return render(request, 'author/create_author.html')
