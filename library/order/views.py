from django.shortcuts import render


def showOrders(request):
    return render(request, 'order/order.html')
