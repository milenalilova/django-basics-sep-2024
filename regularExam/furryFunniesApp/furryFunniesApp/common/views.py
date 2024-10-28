from django.shortcuts import render, redirect

from furryFunniesApp.posts.models import Post
from furryFunniesApp.urils import get_profile


def index(request):
    return render(request, 'common/index.html')


def show_dashboard(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts
    }

    return render(request, 'common/dashboard.html', context)
