from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.startPage, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('author/', include('author.urls'), name='author'),
    path('book/', include('book.urls'), name='book'),
    path('order/', include('order.urls'), name='order'),

]
