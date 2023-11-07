from django.db import models
from account.models import User

# Create your models here.
class LIBRARY(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    
    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        """
        This method is used to save a library.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_library_by_email(cls, email):
        try:
            library = cls.objects.get(user__email=email)
            return library
        except cls.DoesNotExist:
            return None