from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showOrders, name='order'),
    path('all/', views.showOrders, name='all')
]
