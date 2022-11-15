from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


@login_required(login_url='login')
def showAuthors(request):
    authors = Author.objects.all()
    return render(request, 'author/author.html', {'authors': authors})
