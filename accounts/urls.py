from django.urls import path

from accounts import views

urlpatterns = [
    path('signup/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('profile/<int:user_id>', views.profile, name = 'profile'),
]