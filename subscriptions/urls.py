from django.urls import include, path

from .views import subscriptionView

urlpatterns = [
    path('', subscriptionView, name="subscriptions" )
]
