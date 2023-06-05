from django.urls import path

from friends import views

urlpatterns = [
    path('friends', views.friends, name = 'friends' ),
]