from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'comment_text'}))
    class Meta:
        model = Comment
        fields = ['text', ]