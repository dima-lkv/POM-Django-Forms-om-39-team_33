from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


@login_required(login_url='login')
def showAuthors(request):
    print(request.path)
    if request.user.role == 1:
        authors = Author.objects.all()
        return render(request, 'author/author.html', {'authors': authors})
    else:
        return render(request, 'authentication/denied.html')


@login_required(login_url='login')
def createAuthor(request):
    print(request.path)
    return render(request, 'author/create_author.html')
