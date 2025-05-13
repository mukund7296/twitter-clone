from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, PostForm
from .models import Post, Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'posts': posts, 'form': form})


@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'core/profile.html', {'profile': profile})
@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'core/profile.html', {'profile': profile})