from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showOrders, name='order'),
    path('create_order/', views.createOrder, name='create_order'),
    path('remove_order/<int:id>', views.removeOrder, name='remove_order'),
]
