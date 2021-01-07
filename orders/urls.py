from django.contrib import admin
from django.urls import include, path

from .views import OrderItemCreateView

urlpatterns = [
    path('', OrderItemCreateView.as_view(), name="order-create"),
]
