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
    if request.method == 'POST':
        data = {label: data for label, data in request.POST.items() if label != 'csrfmiddlewaretoken' and data}
        user = CustomUser.objects.create_user(**data)
        if user:
            return redirect("login")
    return render(request, 'authentication/reg.html')
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     middle_name = request.POST.get('middle_name')
    #
    #     user = CustomUser.objects.create(email=email, password=password, first_name=first_name,
    #                                      last_name=last_name, middle_name=middle_name, is_active=True)
    #     if user:
    #         user.first_name = user.first_name.lower()
    #         user.last_name = user.last_name.lower()
    #         user.middle_name = user.middle_name.lower()
    #
    #         print('user registerted')
    #         return redirect('home')
    #     else:
    #         print(user)
    #         return HttpResponse('Registration Failed')
    # return render(request, 'authentication/reg.html')


def loginPage(request):
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
        print('USER', user, email, password)

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
