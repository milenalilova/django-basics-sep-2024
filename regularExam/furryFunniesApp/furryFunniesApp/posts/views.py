from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryFunniesApp.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from furryFunniesApp.posts.models import Post
from furryFunniesApp.urils import get_profile


# def create_post(request):
#     profile = get_profile()
#     form = PostCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = profile
#             post.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#         'profile': profile
#     }
#
#     return render(request, 'posts/create-post.html', context)


class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_profile()
        return super().form_valid(form)


# def show_details_post(request, post_id):
#     post = Post.objects.get(pk=post_id)
#
#     context = {
#         'post': post
#
#     }
#
#     return render(request, 'posts/details-post.html', context)


class DetailsPostView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    pk_url_kwarg = 'post_id'


# def edit_post(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     form = PostEditForm(instance=post)
#
#     if request.method == 'POST':
#         form = PostEditForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#         'post': post
#
#     }
#
#     return render(request, 'posts/edit-post.html', context)


class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'post_id'


# def delete_post(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('dashboard')
#
#     context = {
#         'form': form,
#         'post': post
#
#     }
#
#     return render(request, 'posts/delete-post.html', context)
#

class DeletePostView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'post_id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
