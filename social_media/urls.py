from django.urls import path
from social_media import views
urlpatterns = [
    path('posts/<int:user_id>', views.posts, name = 'my_posts'),
    path('create/<int:user_id>', views.create, name = 'create'),
]