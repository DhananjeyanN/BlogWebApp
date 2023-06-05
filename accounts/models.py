from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField()
    dob = models.DateField(null=True, blank=True)
    # friends = models.ManyToManyField(related_name='friends', blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.email}'