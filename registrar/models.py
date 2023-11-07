from django.db import models
from account.models import User

# Create your models here.
class REGISTRAR(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    
    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        """
        This method is used to save a registrar.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_registrar_by_email(cls, email):
        try:
            registrar = cls.objects.get(user__email=email)
            return registrar
        except cls.DoesNotExist:
            return None