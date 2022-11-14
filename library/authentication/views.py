from django.shortcuts import render, redirect
from authentication.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url="/login/")
def startwork(request):
    return render(request, 'authentication/startsession.html')


def startPage(request):
    return render(request, 'authentication/home.html')


def register(request):
    if request.method == 'POST':
        data = {label: data for label, data in request.POST.items() if label != 'csrfmiddlewaretoken' and data}
        user = CustomUser.objects.create_user(**data)
        if user:
            return redirect("authentication:login")
    return render(request, 'authentication/reg.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication:startwork')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'authentication/log.html')


def logoutuser(request):
    logout(request)
    return redirect('authentication:login')
