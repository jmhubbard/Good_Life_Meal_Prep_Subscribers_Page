from django.urls import path

from main.views import UserLoginView, UserLogoutView
from .views import UserCreateView, CustomPasswordChangeView, CustomPasswordChangeDoneView
urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/' , UserLogoutView.as_view(), name='logout'),
    path('create/', UserCreateView.as_view(), name="user_create"),
    path('change_password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('change_password_done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

]