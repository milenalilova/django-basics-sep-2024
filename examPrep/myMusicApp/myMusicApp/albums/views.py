from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from myMusicApp.albums.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from myMusicApp.albums.models import Album
from myMusicApp.profiles.models import Profile


# def add_album(request):
#     form = CreateAlbumForm(request.POST or None)
#     profile = Profile.objects.first()
#
#     if form.is_valid():
#         album = form.save(commit=False)
#         album.owner = profile
#         album.save()
#
#         return redirect('index')
#
#     context = {'form': form}
#
#     return render(request, 'albums/album-add.html', context)


class AddAlbumView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        profile = Profile.objects.first()  # Get the first profile (you can adjust this logic)
        album = form.save(commit=False)
        album.owner = profile  # Assign the owner to the current profile
        album.save()
        return super().form_valid(form)


#     TODO fix the placeholders in the form


# def show_details_album(request, pk):
#     album = Album.objects.get(pk=pk)
#
#     context = {'album': album}
#
#     return render(request, 'albums/album-details.html', context)


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    context_object_name = 'album'


class AlbumEditView(UpdateView):
    model = Album
    form_class = EditAlbumForm
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('index')


def delete_album(request, pk):
    return render(request, 'albums/album-delete.html')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = DeleteAlbumForm
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
