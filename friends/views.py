from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from friends.models import Friend


# Create your views here.
def add_friend(request, friend_id):
    user = request.user
    new_friend = User.objects.get(id=friend_id)
    Friend.make_friend(user, new_friend)
    print(user.friend_set.all(), 'adding friend')

    return redirect('dashboard', username = user.username)

def make_friend():
    pass

def friends(request):
    friends = Friend.objects.all()
    context = {'friends':friends}
    return render(request, 'friends.html', context)