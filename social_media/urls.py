from django.urls import path
from social_media import views
urlpatterns = [
    path('posts/<int:user_id>', views.posts, name = 'my_posts'),
    path('create/<int:user_id>', views.create, name = 'create'),
    path('edit/<int:post_id>', views.edit_post, name = 'edit_post'),
    path('delete/<int:post_id>', views.delete_post, name = 'delete_post'),
    path('post_detail/<int:post_id>', views.post_detail, name = 'post_detail'),
    path('like_post/<int:post_id>', views.like_post, name = 'like_post'),
]