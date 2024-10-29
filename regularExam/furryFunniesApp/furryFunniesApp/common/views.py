from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from furryFunniesApp.posts.models import Post
from furryFunniesApp.urils import get_profile


# def index(request):
#     return render(request, 'common/index.html')


class IndexView(TemplateView):
    template_name = 'common/index.html'


# def show_dashboard(request):
#     all_posts = Post.objects.all()
#
#     context = {
#         'all_posts': all_posts
#     }
#
#     return render(request, 'common/dashboard.html', context)


class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'all_posts'
