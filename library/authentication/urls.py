from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.startPage),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),

]
