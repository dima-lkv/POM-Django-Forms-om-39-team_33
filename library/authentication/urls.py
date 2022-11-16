from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.startPage, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.pageUser, name='user'),
    path('author/', include('author.urls')),
    path('book/', include('book.urls')),
    path('order/', include('order.urls')),

]
