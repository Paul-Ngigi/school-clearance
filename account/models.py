from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):      
    ROLE_CHOICES = (
        ('CHAIRMAN_OF_DEPARTMENT', 'Chairman of Department'),
        ('LIBRARY', 'Library'),
        ('SPORTS_AND_ENTERTAINMENT', 'Sports and entertainment'),
        ('HOSTELS', 'Hostels'),
        ('FINANCE', 'Finance'), 
        ('DEAN_OF_STUDENTS', 'Dean of Students'),
        ('REGISTRAR', 'Registrar'),   
        ('STUDENT', 'Student')
    )
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),       
    )      
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(choices=ROLE_CHOICES, max_length=30)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=8)
    id_number = models.IntegerField(default=0)                
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)                 
    
    @classmethod    
    def find_user_by_email(cls, email):
        user = cls.objects.get(email=email)
        return user
    
    def get_user_role(self):        
        return self.role
    
    def get_user_sex(self):
        return self.sex
    
    def get_user_id_number(self):
        return self.id_number
        
        
        