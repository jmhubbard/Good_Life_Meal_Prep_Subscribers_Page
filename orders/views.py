from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Order, OrderItem

class OrderItemCreateView(CreateView):
    model = OrderItem
    fields =['name', 'quantity']
