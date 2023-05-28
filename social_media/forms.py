from django import forms
from social_media.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'image', 'category', 'pub_date']
