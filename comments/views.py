from django.shortcuts import render, get_object_or_404, redirect
from comments.forms import CommentForm
from social_media.models import Post


# Create your views here.

def add_comment(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', post_id = post.id)

    else:
        form = CommentForm()

    context = {'form':form, 'post':post}
    return render(request, 'comments/add_comment.html', context=context)
