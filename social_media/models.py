from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='Posts/Images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True) #related name allows the access using all posts liked by user ex: User.likes.all()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'Title: {self.title} Posted By: {self.author}'

    class Meta:
        ordering = ['title']





