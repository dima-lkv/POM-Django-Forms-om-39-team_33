from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showBooks, name='book'),
    path('ordered/<str:pk>/', views.showOrderedBooks, name='showOrderedBooks'),
    path('id/<int:id>/', views.showSpecificBook, name='showSpecificBook'),
]
