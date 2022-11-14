from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.startPage),
    path('register/', views.register_page),
    path('login/', views.login_page),

]
