from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .backend import CustomAuthentication


# from django.contrib.auth.forms import UserCreationForm


def startPage(request):
    return render(request, 'authentication/home.html')


def registerPage(request):
    if request.user.is_authenticated:
        text = 'You are already logged in'
        return render(request, 'authentication/denied.html', {'text': text})

    if request.method == 'POST':
        data = {label: data for label, data in request.POST.items() if label != 'csrfmiddlewaretoken' and data}
        user = CustomUser.objects.create_user(**data)
        if user:
            return redirect("login")
    return render(request, 'authentication/reg.html')


def loginPage(request):
    if request.user.is_authenticated:
        text = 'You are already logged in'
        return render(request, 'authentication/denied.html', {'text': text})

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # try:
        #     user = CustomUser.objects.get(email=email)
        #     user = CustomUser.objects.get(password=password)
        # except:
        #     print('User does not exist')
        #     messages.error(request, 'User does not exist.')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password does not exist.')

    return render(request, 'authentication/log.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
