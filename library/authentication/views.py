from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# from django.contrib.auth.forms import UserCreationForm


def startPage(request):
    return render(request, 'authentication/home.html')


def registerPage(request):
    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.name = user.name.lower()
    #         user.surname = user.surname.lower()
    #         user.patronymic = user.patronymic.lower()
    #         user.save()
    #         login(request.user)
    #         return redirect(request, 'home')
    return render(request, 'authentication/reg.html')


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            user = CustomUser.objects.get(password=password)
            print('user logged')
        except:
            print('User does not exist')
            messages.error(request, 'User does not exist.')

        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print('user authenticated')
            return redirect('home')
        else:
            messages.error(request, 'Email or Password does not exist.')

    return render(request, 'authentication/log.html')


def logoutUser(request):
    logout(request)
    return redirect('login')