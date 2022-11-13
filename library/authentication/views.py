from django.shortcuts import render


def startPage(request):
    return render(request, 'authentication/base.html')
