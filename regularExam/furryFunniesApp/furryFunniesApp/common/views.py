from django.shortcuts import render, redirect

from furryFunniesApp.posts.models import Post
from furryFunniesApp.urils import get_profile


def index(request):
    profile = get_profile()

    context = {'profile': profile}

    return render(request, 'common/index.html', context)


def show_dashboard(request):
    profile = get_profile()
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts,
        'profile': profile
    }

    return render(request, 'common/dashboard.html', context)
