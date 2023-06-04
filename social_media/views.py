from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from Core.models import SiteProfile
from accounts.forms import EditPostForm
from comments.forms import CommentForm
from comments.models import Comment
from social_media.models import Post, Category


# Create your views here.
def posts(request, user_id):
    profile = SiteProfile.objects.all().first()
    user_posts = Post.objects.filter(author = user_id)
    context = {'posts':user_posts, 'profile':profile}
    return render(request,'accounts/dashboard.html', context=context)

def create(request, user_id):
    categories = Category.objects.all()
    profile = SiteProfile.objects.all().first()
    context = {'categories':categories, 'profile':profile}
    if request.method == 'POST':
        title = request.POST.get('Title')
        author_id = int(request.POST.get('Author'))
        author = User.objects.filter(id=author_id).first()
        content = request.POST.get('Content')
        image = request.FILES.get('Image')
        category_id = request.POST.get('Category')
        category = Category.objects.filter(id=category_id).first()
        post = Post(title = title, author = author, content= content, image = image, category = category)
        post.save()
        messages.success(request, 'Posted successfully')
        return redirect('my_posts', user_id=post.author.id)
    return render(request, 'accounts/create_post.html', context=context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('index')
    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Saved!!!')
            return redirect('my_posts', user_id=post.author.id)
    else:
        form = EditPostForm(instance=post)
    profile = SiteProfile.objects.all().first()
    context = {'form':form, 'profile':profile}
    return render(request, 'accounts/edit_post.html', context=context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('my_posts', user_id=post.author.id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post Deleted!!!')
        return redirect('my_posts', user_id=post.author.id)
    context = {'post':post}
    return render(request, 'SocialMedia/delete_post.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments= Comment.objects.filter(post = post.id).order_by('-pub_date')[:5]
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    form = CommentForm()
    context = {'post': post, 'comments':comments, 'CommentForm':form, 'new_comment':new_comment}
    return render(request, 'SocialMedia/post_detail.html', context=context)

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('home')




