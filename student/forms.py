from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Student
from account.models import User
from clearance.models import Clearance

academic_years = (
    ('1st', 'First',),
    ('2nd', 'Second'),
    ('3rd', 'Third'),
    ('4th', 'Fourth')
)

class StudentSignUpForm(forms.ModelForm):           
    class Meta:
        model = Student
        fields = ['school', 'department', 'program', 'academic_year']        