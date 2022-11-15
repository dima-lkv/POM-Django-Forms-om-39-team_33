from django.shortcuts import render
from .models import Order

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showOrders(request):
    if request.user.role != 1:
        text = 'You have no permission to view this page'
        return render(request, 'authentication/denied.html', {'text': text})
    orders = Order.objects.all()
    return render(request, 'order/order.html', {'orders': orders})
