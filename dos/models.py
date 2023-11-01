from django.db import models
from account.models import User

# Create your models here.
class DEAN_OF_STUDENTS(models.Model):        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """
        This method is used to save a dos.
        """
        super().save(*args, **kwargs)

    @classmethod
    def find_dos_by_username(cls, username):
        try:
            dos = cls.objects.get(user__username=username)
            return dos
        except cls.DoesNotExist:
            return None