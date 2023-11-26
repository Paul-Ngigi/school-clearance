from django.urls import path
from .views import SignUpView, SignInView, SignOutView, ResetPasswordView

urlpatterns = [    
    path('signup', SignUpView.as_view(), name='signup_view'),    
    path('login', SignInView.as_view(), name='login_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
    path('reset-password/', ResetPasswordView.as_view(), name='resetpass_view'),
]
