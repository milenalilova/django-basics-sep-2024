from django.shortcuts import render, redirect

from furryFunniesApp.authors.forms import AuthorCreateForm, AuthorEditForm, AuthorDeleteForm
from furryFunniesApp.posts.models import Post
from furryFunniesApp.urils import get_profile


def create_author(request):
    form = AuthorCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'authors/create-author.html', context)


def show_details_author(request):
    profile = get_profile()
    published_posts = profile.post_set.count()
    last_updated_post = Post.objects.order_by('-updated_at').first()

    context = {
        'profile': profile,
        'published_posts': published_posts,
        'last_updated_post': last_updated_post
    }

    return render(request, 'authors/details-author.html', context)


def edit_author(request):
    profile = get_profile()
    form = AuthorEditForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details author')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'authors/edit-author.html', context)


def delete_author(request):
    profile = get_profile()
    form = AuthorDeleteForm(request.POST or None)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'authors/delete-author.html', context)
