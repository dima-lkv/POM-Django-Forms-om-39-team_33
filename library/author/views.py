from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


@login_required(login_url='login')
def showAuthors(request):
    if request.user.role == 1:
        authors = Author.objects.all()
        return render(request, 'author/author.html', {'authors': authors})
    else:
        return render(request, 'authentication/denied.html')
        return HttpResponse('You have no permission to view this page.')


@login_required(login_url='login')
def createAuthor(request):
    pass
