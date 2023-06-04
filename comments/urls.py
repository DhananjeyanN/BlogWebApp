from django.urls import path

from comments import views

urlpatterns = [
    path('comment/<int:post_id>', views.add_comment, name = 'add_comment')
]