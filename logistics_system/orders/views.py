from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



def order_list(request):
    """Список всіх замовлень"""
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def create_order(request):
    """Створення нового замовлення"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})

def update_order(request, order_id):
    """Редагування існуючого замовлення"""
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Замовлення успішно оновлено!')
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/update_order.html', {'form': form, 'order': order})

def delete_order(request, order_id):
    """Видалення замовлення"""
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Замовлення успішно видалено!')
        return redirect('order_list')
    return render(request, 'orders/delete_order.html', {'order': order})

def search_orders(request):
    """Пошук замовлень"""
    query = request.GET.get('query')
    orders = Order.objects.all()

    if query:
        orders = orders.filter(title__icontains=query)

    return render(request, 'orders/search_orders.html', {'orders': orders, 'query': query})