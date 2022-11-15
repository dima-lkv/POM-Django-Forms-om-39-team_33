from django.shortcuts import render
from .models import Order

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showOrders(request):
    orders = Order.objects.all()
    return render(request, 'order/order.html', {'orders': orders})
