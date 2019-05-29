from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Order
from .forms import OrderForm
from meals.models import Meal

# Create your views here.


def make_order(request, id):
    if request.method == "POST":
        form = OrderForm(request.POST)
        meal = get_object_or_404(Meal, id=id)
        if form.is_valid():
            # form.save()
            form.save(commit=False)
            quantity = form.cleaned_data['quantity']
            requester = form.cleaned_data['requester']
            order, status = Order.objects.get_or_create(meal=meal, quantity=quantity, requester=requester)

            print(quantity)
            print(requester)
            context = {'order': order, 'form': form}
            return render(request, 'orders/order_submitted.html', context)

    else:
        form = OrderForm()

    return render(request, 'orders/order_submitted.html')



