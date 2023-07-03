from django.db import models
from django.contrib.auth.models import AbstractUser




class Roles(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class User(AbstractUser):
    roles = models.ForeignKey(Roles, on_delete=models.PROTECT, null=True ,default = 2 )



class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT ,related_name='userprofile')
    profession = models.CharField(max_length=255)
    profilePic = models.ImageField(upload_to='recipe/images')
    verification_code = models.CharField(max_length=100)
 


