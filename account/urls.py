from django.urls import path
from .views import SignUpView, SignInView, SignOutView

urlpatterns = [    
    path('signup', SignUpView.as_view(), name='signup_view'),    
    path('login', SignInView.as_view(), name='login_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
]
