from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showAuthors, name='author'),
    path('create_author/', views.createAuthor, name='create_author'),
    path('remove_author/<int:id>', views.removeAuthor, name='remove_author'),

]
