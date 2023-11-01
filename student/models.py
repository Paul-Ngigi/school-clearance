from django.db import models
from account.models import User

# Create your models here.
class Student(models.Model):    
    ACADEMIC_YEAR_CHOICES = (
        ('FIRST', 'first'),
        ('SECOND', 'second'),
        ('THIRD', 'third'),
        ('FOURTH', 'fourth'),       
    )  
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school = models.CharField(max_length=30, blank=False)    
    department = models.CharField(max_length=30, blank=False)    
    program = models.CharField(max_length=30, blank=False)    
    academic_year = models.CharField(max_length=15, choices=ACADEMIC_YEAR_CHOICES, blank=False)    
    year = models.DateField(auto_now_add=True)  
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        This method is used to save a student.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_student_by_email(cls, email):
        try:
            student = cls.objects.get(user__email=email)
            return student
        except cls.DoesNotExist:
            return None