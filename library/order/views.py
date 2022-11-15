from django.shortcuts import render
from .models import Order

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showOrders(request):
    if request.user.role == 1:
        orders = Order.objects.all()
        return render(request, 'order/order.html', {'orders': orders})
    else:
        return render(request, 'authentication/denied.html')
