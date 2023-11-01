from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

ROLE_CHOICES = (
        ('CHAIRMAN_OF_DEPARTMENT', 'chairman_of_department'),
        ('LIBRARY', 'library'),
        ('SPORTS_AND_ENTERTAINMENT', 'sports_and_entertainment'),
        ('HOSTELS', 'hostels'),
        ('FINANCE', 'finance'),
        ('DEAN_OF_STUDENTS', 'dean_of_students'),
        ('REGISTRAR', 'registrar'),   
        ('STUDENT', 'student')
    )   


# Authentication forms
class LoginForm(forms.Form):
    email = forms.CharField(required=True)    
    password = forms.CharField(required=True)    

class UserForm(UserCreationForm):        
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'role', 'sex', 'id_number')                
