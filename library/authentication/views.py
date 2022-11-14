from django.shortcuts import render, redirect
from authentication.models import CustomUser


def startPage(request):
    return render(request, 'authentication/home.html')


def register(request):
    if request.method == 'POST':
        data = {label: data for label, data in request.POST.items() if label != 'csrfmiddlewaretoken' and data}
        user = CustomUser.objects.create_user(**data)
        if user:
            return redirect("authentication:login")
    return render(request, 'authentication/reg.html')


def login(request):
    return render(request, 'authentication/log.html')
