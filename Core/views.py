from django.http import HttpResponse
from django.shortcuts import render

from Core.models import SiteProfile
from social_media.models import Post


# Create your views here.
def home(request):
    profile = SiteProfile.objects.all().first()
    posts = Post.objects.all().order_by('-pub_date') # retrieves all objects from database
    context = {'profile': profile, 'posts': posts}
    return render(request, 'core/index.html', context=context)


def about(request):
    profile = SiteProfile.objects.all().first()
    context = {'profile': profile}
    return render(request, 'core/about.html', context=context)


def contact(request):
    profile = SiteProfile.objects.all().first()
    context = {'profile': profile}
    return render(request, 'core/contact.html', context=context)
