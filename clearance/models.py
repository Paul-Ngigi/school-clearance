from django.db import models
from django.conf import settings
from student.models import Student
from account.models import User

# Create your models here.        
class Clearance(models.Model):    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)        
    status = models.CharField(max_length=30, default='Initiated')    
    completed = models.BooleanField(default=False)
    initiated_at = models.DateTimeField(auto_now_add=True)    
    
    @classmethod
    def get_clearance_by_id(cls,id):
        try:
            clearance = cls.objects.get(id=id)
            return clearance
        except:
            return None            
    
class Review(models.Model):
    clearance = models.ForeignKey(Clearance, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)