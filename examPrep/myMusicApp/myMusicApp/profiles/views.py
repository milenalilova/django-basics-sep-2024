from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import DetailView, DeleteView

from myMusicApp.profiles.models import Profile


class ProfileDetailsView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        profile = Profile.objects.first()
        return profile


def delete_profile(request):
    return render(request, 'profiles/profile-delete.html')


class ProfileDeleteView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        profile = Profile.objects.first()
        return profile
