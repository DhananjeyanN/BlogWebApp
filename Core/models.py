from django.db import models


# Create your models here.
class SiteProfile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    developed_by = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='core_images/')
    year_started = models.DateField()

    def __str__(self):
        return self.name

