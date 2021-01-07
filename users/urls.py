from django.urls import path

from main.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login")
]