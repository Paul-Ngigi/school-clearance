from django.db import models
from account.models import User

# Create your models here.
class CHAIRMAN_OF_DEPARTMENT(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        This method is used to save a cod.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_cod_by_username(cls, username):
        try:
            cod = cls.objects.get(user__username=username)
            return cod
        except cls.DoesNotExist:
            return None