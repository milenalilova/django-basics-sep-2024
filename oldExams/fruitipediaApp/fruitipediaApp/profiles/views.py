from django.shortcuts import render, redirect

from fruitipediaApp.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from fruitipediaApp.profiles.models import Profile
from fruitipediaApp.utils import get_profile


def create_profile(request):
    profile = Profile()
    form = ProfileCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/create-profile.html', context)


def show_details_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    form = ProfileEditForm(instance=profile)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    form = ProfileDeleteForm(request.POST or None)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profiles/delete-profile.html', context)
