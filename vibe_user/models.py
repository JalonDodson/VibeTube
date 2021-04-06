from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=120)
    display_name = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextAreaField(blank=True)
    password = models.PasswordInput()
    followers = models.ManyToManyField('self', symmetrical=False)
    following = models.ManyToManyField('self', symmetrical=False)
    likes = models.IntegerField(null=True, blank=True)
    video = models.ManyToManyField('self', symmetrical=False)
    sound = models.ManyToManyField('self', symmetrical=False)
    liked = models.ForeignKey(Video, on_delete=models.CASCADE)
    profile_photo = models.ImageField(blank=True)
