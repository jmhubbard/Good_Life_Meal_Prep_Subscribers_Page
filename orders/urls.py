from django.contrib import admin
from django.urls import include, path

from .views import OrderItemCreateView



from recipes.views import menu, createOrder

urlpatterns = [
    # path('', OrderItemCreateView.as_view(), name="order-create"),
    # path('', menu, name="menu" )
    path('', createOrder, name="menu" )



]
