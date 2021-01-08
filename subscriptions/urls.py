from django.urls import include, path

from .views import subscriptionView, SubscriptionUpdate

urlpatterns = [
    path('', subscriptionView, name="subscriptions" ),
    path('update/<int:pk>/', SubscriptionUpdate.as_view(), name='subscription-update')
]
