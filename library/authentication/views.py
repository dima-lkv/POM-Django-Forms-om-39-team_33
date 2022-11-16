from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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
            messages.error(request, 'Failed to log in. Try again')

    return render(request, 'authentication/log.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def pageUser(request):
    # if request.user.role != 1:
    #     text = 'You have no permission to view this page'
    #     return render(request, 'authentication/denied.html', {'text': text})
    users = CustomUser.objects.all()
    return render(request, 'authentication/user.html', {'users': users})

def oneUser(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, 'authentication/specificUser.html', {'user': user})

