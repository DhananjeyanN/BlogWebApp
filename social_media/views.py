from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Core.models import SiteProfile
from social_media.models import Post, Category


# Create your views here.
def posts(request, user_id):
    profile = SiteProfile.objects.all().first()
    user_posts = Post.objects.filter(author = user_id)
    context = {'posts':user_posts, 'profile':profile}
    return render(request,'accounts/dashboard.html', context=context)

def create(request, user_id):
    categories = Category.objects.all()
    context = {'categories':categories}
    print(request.POST)
    if request.method == 'POST':
        title = request.POST.get('Title')
        author_id = int(request.POST.get('Author'))
        author = User.objects.filter(id=author_id).first()
        content = request.POST.get('Content')
        image = request.POST.get('Image')
        image = 'Posts/Images/' + image
        category_id = request.POST.get('Category')
        category = Category.objects.filter(id=category_id).first()
        post = Post(title = title, author = author, content= content, image = image, category = category)
        post.save()
        messages.success(request, 'Posted successfully')
        return redirect('dashboard')
    return render(request, 'accounts/create_post.html', context=context)