from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.startPage, name="home-page"),
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logoutuser, name='logout'),
    path('startwork/', views.startwork, name="startwork"),

]
