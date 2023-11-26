from django.urls import path
from .views import send_mails

urlpatterns = [
    path('send-mail', send_mails, name="send_mail"),
]