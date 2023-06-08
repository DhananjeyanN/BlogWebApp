from django.urls import path

from friends import views

urlpatterns = [
    path('friends', views.friends, name = 'friends' ),
    path('add_friend/<int:friend_id>', views.add_friend, name = 'add_friend' ),
    path('remove_friend/<int:friend_id>', views.remove_friend, name = 'remove_friend' ),
]