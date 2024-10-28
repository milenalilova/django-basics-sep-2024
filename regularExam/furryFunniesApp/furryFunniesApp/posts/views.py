from django.shortcuts import render, redirect

from furryFunniesApp.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from furryFunniesApp.posts.models import Post
from furryFunniesApp.urils import get_profile


def create_post(request):
    profile = get_profile()
    form = PostCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = profile
            post.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'posts/create-post.html', context)


def show_details_post(request, post_id):
    profile = get_profile()
    post = Post.objects.get(pk=post_id)

    content = {
        'post': post,
        'profile': profile
    }

    return render(request, 'posts/details-post.html', content)


def edit_post(request, post_id):
    profile = get_profile()
    post = Post.objects.get(pk=post_id)
    form = PostEditForm(instance=post)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'post': post,
        'profile': profile
    }

    return render(request, 'posts/edit-post.html', context)


def delete_post(request, post_id):
    profile = get_profile()
    post = Post.objects.get(pk=post_id)
    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'post': post,
        'profile': profile
    }

    return render(request, 'posts/delete-post.html', context)
