from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
     username = models.CharField(max_length=150, unique=True)
     first_name = models.CharField(max_length=150, blank=True)
     last_name = models.CharField(max_length=150, blank=True)
     password = models.CharField(max_length=128)
     is_active = models.BooleanField(default=True)
     is_staff = models.BooleanField(default=False)
     is_superuser = models.BooleanField(default=False)
     is_verified = models.BooleanField(default=False)
     is_admin = models.BooleanField(default=False)
     is_author = models.BooleanField(default=False)
     is_subscriber = models.BooleanField(default=False)
     is_editor = models.BooleanField(default=False)
     is_moderator = models.BooleanField(default=False)
     is_contributor = models.BooleanField(default=False)
     is_guest = models.BooleanField(default=False)
     email = models.EmailField(unique=True)
     bio = models.TextField(blank=True)
     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
     location = models.CharField(max_length=255, blank=True)
     date_of_birth = models.DateField(null=True, blank=True)
     date_joined = models.DateTimeField(auto_now_add=True)
     last_login = models.DateTimeField(null=True, blank=True)

     def __str__(self):
        return self.username
  
      