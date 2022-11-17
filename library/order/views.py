import datetime

from django.shortcuts import render, redirect

from book.models import Book
from .models import Order
from authentication.models import CustomUser

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showOrders(request):
    if request.user.role != 1:
        orders = Order.objects.filter(id=request.user.id)
        return render(request, 'order/order.html', {'orders': orders})
    orders = Order.objects.all()
    return render(request, 'order/order.html', {'orders': orders})


def createOrder(request):
    if request.method == 'POST':
        user_id = int(request.POST.get('user_id')) if request.POST.get('user_id') else request.user.id
        book_id = request.POST.get('book_id')
        user = CustomUser.get_by_id(user_id)
        book = Book.get_by_id(book_id)
        print(user_id)
        print(book_id)

        plated_end_at = request.POST.get('plated_end_at')
        plated_end_at = plated_end_at.split('-')
        time = datetime.datetime.now().replace(year=int(plated_end_at[0]), month=int(plated_end_at[1]), day=int(plated_end_at[2]))
        our_order = Order.create(user, book, plated_end_at=time)
    return render(request, 'order/create_order.html')


def removeOrder(request):
    order_id = request.POST.get('order_id')
    Order.delete_by_id(order_id)
    return redirect('order')

