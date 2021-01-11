from django.urls import path

from main.views import UserLoginView, UserLogoutView
from .views import (UserSignUpView, CustomPasswordChangeView,
                    CustomPasswordChangeDoneView, CustomPasswordResetView,
                    CustomPasswordResetDoneView, CustomPasswordResetConfirmView,
                    CustomPasswordResetCompleteView) 
urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/' , UserLogoutView.as_view(), name='logout'),
    path('create/', UserSignUpView.as_view(), name="user_sign_up"),
    path('change_password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('change_password_done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]