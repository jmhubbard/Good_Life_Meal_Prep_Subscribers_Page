from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Recipe
from orders.models import Order, OrderItem

# def menu(request):
#     current_user = request.user
#     recipes = Recipe.objects.all()
#     context ={
#         'current_user': current_user,
#         'recipes': recipes
#     }

#     return render(request, 'recipes/menu.html', context)

def menu(request):
    current_user = request.user
    recipes = Recipe.objects.all()
    order = Order(user=current_user)
    orderItems = []
    for item in recipes:
        OItem = OrderItem(name=item, order=order)
        orderItems.append(OItem)

    context ={
        'current_user': current_user,
        'recipes': recipes,
        'order': order,
        'orderItems': orderItems

    }

    return render(request, 'recipes/menu.html', context)


def createOrder(request):
    order = Order.objects.get(id=35)
    OrderItemFormSet = inlineformset_factory(Order, OrderItem, fields=('name', 'quantity'), max_num=3)
    if request.method == 'POST':
        formset = OrderItemFormSet(request.POST, instance=order)
        if formset.is_valid():
            # order.save()
            formset.save()
            return redirect('/')
    else:
        formset = OrderItemFormSet(instance=order)    
    
    context = {'formset': formset}
    return render(request, 'recipes/order_form.html', context)