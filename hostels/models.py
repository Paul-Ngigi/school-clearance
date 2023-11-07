from django.db import models
from account.models import User

# Create your models here.
class HOSTEL(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    
    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        """
        This method is used to save a hostel.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_hostel_by_email(cls, email):
        try:
            hostel = cls.objects.get(user__email=email)
            return hostel
        except cls.DoesNotExist:
            return None