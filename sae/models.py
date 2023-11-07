from django.db import models
from account.models import User

# Create your models here.
class SPORTS_AND_ENTERTAINMENT(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    
    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        """
        This method is used to save a sae.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_sae_by_email(cls, email):
        try:
            sae = cls.objects.get(user__email=email)
            return sae
        except cls.DoesNotExist:
            return None