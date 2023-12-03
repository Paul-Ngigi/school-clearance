from django.urls import path
from .views import SignUpView, SignInView, SignOutView, ResetPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [    
    path('signup', SignUpView.as_view(), name='signup_view'),    
    path('login', SignInView.as_view(), name='login_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
     path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
