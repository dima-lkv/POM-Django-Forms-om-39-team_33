from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showBooks, name='book'),
    path('<str:pk>/', views.showOrderedBooks, name='showOrderedBooks'),
    path('<int:id>', views.showSpecificBook, name='showSpecificBook'),
]
