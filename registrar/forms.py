from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from account.models import User
from clearance.models import Clearance, Review


class ReviewForm(forms.ModelForm):           
    class Meta:
        model = Review
        fields = ['approved', 'rejected', 'reason']        