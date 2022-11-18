import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from book.models import Book
from .models import Order
from authentication.models import CustomUser
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def showOrders(request):
    if request.user.role != 1:
        orders = Order.objects.filter(user_id=request.user.id)
        return render(request, 'order/order.html', {'orders': orders})
    orders = reversed(Order.objects.order_by('id'))
    return render(request, 'order/order.html', {'orders': orders})


def createOrder(request):
    if request.method == 'POST':
        user_id = int(request.POST.get('user_id')) if request.POST.get('user_id') else request.user.id
        book_id = request.POST.get('book_id')
        if not Book.get_by_id(book_id):
            messages.error(request, 'No book with such id.')
            return redirect('create_order')
        user = CustomUser.get_by_id(user_id)
        book = Book.get_by_id(book_id)
        plated_end_at = request.POST.get('plated_end_at')
        try:
            time = datetime.datetime.now().replace(day=datetime.datetime.now().day+int(plated_end_at))
        except:
            time = datetime.datetime.now().replace(month=datetime.datetime.now().month+1,
                                                   day=datetime.datetime.now().day+(int(plated_end_at)-30))

        if book.count <= 0:
            messages.error(request, 'The book was disassembled.')
            return redirect('create_order')
        book.update(count=book.count-1)
        Order.create(user, book, plated_end_at=time)
    return render(request, 'order/create_order.html')


def removeOrder(request, id):
    our_order = Order.objects.get(id=id)
    our_order.update(end_at=datetime.datetime.now())
    Book.get_by_id(our_order.book_id).update(count=Book.get_by_id(our_order.book_id).count+1)
    return redirect('order')

