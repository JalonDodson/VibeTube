from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Viber(AbstractUser):
    display_name = models.CharField(max_length=120, null=True, blank=True)
    bio = models.TextField()
    followers = models.ManyToManyField('self', symmetrical=False, related_name='viber_followers')
    following = models.ManyToManyField('self', symmetrical=False, related_name='viber_following')
    video = models.ManyToManyField('self', symmetrical=False, related_name='viber_video')
    sound = models.ManyToManyField('self', symmetrical=False, related_name='viber_sound')
    # profile_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.username