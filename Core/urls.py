from django.urls import path

from Core import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('about/', views.home, name = 'about' ),
    path('contact/', views.home, name = 'contact' ),
]