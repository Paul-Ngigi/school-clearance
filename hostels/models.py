from django.db import models
from account.models import User

# Create your models here.
class HOSTEL(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        This method is used to save a hostel.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_hostel_by_username(cls, username):
        try:
            hostel = cls.objects.get(user__username=username)
            return hostel
        except cls.DoesNotExist:
            return None