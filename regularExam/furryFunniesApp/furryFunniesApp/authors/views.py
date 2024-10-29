from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryFunniesApp.authors.forms import AuthorCreateForm, AuthorEditForm, AuthorDeleteForm
from furryFunniesApp.authors.models import Author
from furryFunniesApp.posts.models import Post
from furryFunniesApp.urils import get_profile


# def create_author(request):
#     form = AuthorCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'authors/create-author.html', context)

class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dashboard')


# def show_details_author(request):
#     profile = get_profile()
#     published_posts = profile.post_set.count()
#     last_updated_post = Post.objects.order_by('-updated_at').first()
#
#     context = {
#         'profile': profile,
#         'published_posts': published_posts,
#         'last_updated_post': last_updated_post
#     }
#
#     return render(request, 'authors/details-author.html', context)


class DetailsAuthorView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        profile = self.get_object()
        published_posts = profile.post_set.count()
        last_updated_post = Post.objects.order_by('-updated_at').first()

        context['published_posts'] = published_posts
        context['last_updated_post'] = last_updated_post

        return context


# def edit_author(request):
#     profile = get_profile()
#     form = AuthorEditForm(request.POST or None, instance=profile)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('details author')
#     context = {
#         'profile': profile,
#         'form': form
#     }
#     return render(request, 'authors/edit-author.html', context)

class EditAuthorView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details author')

    def get_object(self):
        return get_profile()


# def delete_author(request):
#     profile = get_profile()
#     form = AuthorDeleteForm(request.POST or None)
#     if request.method == 'POST':
#         profile.delete()
#         return redirect('index')
#
#     context = {
#         'profile': profile,
#         'form': form
#     }
#
#     return render(request, 'authors/delete-author.html', context)


class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')
    context_object_name = 'profile'

    def get_object(self):
        return get_profile()
