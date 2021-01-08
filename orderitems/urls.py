from django.urls import include, path

from .views import orderItemsView, OrderItemUpdate

urlpatterns = [
    path('', orderItemsView, name="orderitems" ),
    path('update/<int:pk>/', OrderItemUpdate.as_view(), name='orderitem-update')
]