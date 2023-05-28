from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Core.models import SiteProfile
from django.contrib import messages, auth

from accounts.forms import RegistrationForm
from social_media.models import Post


# Create your views here.

def register_(request):
    profile = SiteProfile.objects.all().first()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        #print(form)
        if form.is_valid():
            form.password = request.POST.get('password')
            form.save()
            #print(user.password)
            return redirect('login')

    else:
        form = RegistrationForm()

    context = {'profile':profile, 'form':form}
    return render(request, 'accounts/register.html', context=context)


def login(request):
    profile = SiteProfile.objects.all().first()
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

            print('hello')
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Logged In!!!")
                return redirect('my_posts', user.id)
        else:
            messages.error(request, "Incorrect Login")
            return redirect('login')
    form = AuthenticationForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'accounts/login.html', context=context)


def logout(request):
    # profile = SiteProfile.objects.all().first()
    # context = {'profile':profile}
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out!!!')
    return redirect('login')


def dashboard(request):
    profile = SiteProfile.objects.all().first()
    context = {'profile':profile}
    return render(request, 'accounts/dashboard.html', context=context)


def register(request):
    profile = SiteProfile.objects.all().first()
    form = RegistrationForm()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if password1 != password2:
            print('passwords do not match')
            messages.error(request,'passwords do not match')
            return redirect('register')
        elif len(password1) < 6:
            print('password must be at least 6 characters long')
            messages.error(request,'password must be at least 6 characters long')
            return redirect('register')
        elif User.objects.filter(username= username).exists():
            print('username is taken')
            messages.error(request,'username is taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email, password=password1,first_name=first_name, last_name=last_name)
            user.save()
            print('registered successfully')
            messages.success(request, 'registered successfully')
            return redirect('login')

    context = {'profile':profile, 'form':form}
    return render(request, 'accounts/register.html', context=context)

def login_(request):
    #form = LoginForm()
    profile = SiteProfile.objects.all().first()
    context = {'profile':profile, 'form':form}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "Logged In!!!")
            return redirect('my_posts', user.id)
        else:
            messages.error(request, "Incorrect Login")
            return redirect('login')

    return render(request, 'accounts/login.html', context=context)
