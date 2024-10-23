from django.shortcuts import render, redirect

from worldOfSpeedApp.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from worldOfSpeedApp.utils import get_profile


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, 'profiles/profile-create.html', context)


def show_profile_details(request):
    profile = get_profile()

    context = {'profile': profile}

    return render(request, 'profiles/profile-details.html', context)


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

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    form = ProfileDeleteForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profiles/profile-delete.html', context)
