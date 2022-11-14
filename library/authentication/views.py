from django.shortcuts import render


def startPage(request):
    return render(request, 'authentication/home.html')


def register_page(request):
    return render(request, 'authentication/reg.html')


def login_page(request):
    return render(request, 'authentication/log.html')
