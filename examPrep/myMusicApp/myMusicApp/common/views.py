from django.shortcuts import render, redirect

from myMusicApp.albums.models import Album
from myMusicApp.common.forms import CreateProfileForm
from myMusicApp.profiles.models import Profile


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'no_nav': True}

    return render(request, 'common/home-no-profile.html', context)


def index(request):
    profile = Profile.objects.first()

    if profile is None:
        return create_profile(request)

    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}

    return render(request, 'common/home-with-profile.html', context)
