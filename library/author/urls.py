from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showAuthors, name='author'),
    path('', views.createAuthor, name='create_author'),
]
