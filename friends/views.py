from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from friends.models import Friend


# Create your views here.
def add_friend(request, friend_id):
    user = request.user
    new_friend = User.objects.get(id=friend_id)
    friend_list,created=Friend.objects.get_or_create(current_user = user)
    friend_list.users.add(new_friend)
    return redirect('dashboard')

def remove_friend(request, friend_id):
    user = request.user
    new_friend = User.objects.get(id=friend_id)
    friend_list,created = Friend.objects.get_or_create(current_user = user)
    friend_list.users.remove(new_friend)
    return redirect('dashboard')

def make_friend():
    pass

def friends(request):
    friends = Friend.objects.all()
    context = {'friends':friends}
    return render(request, 'friends.html', context)