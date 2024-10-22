from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tastyRecipesApp.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from tastyRecipesApp.profiles.models import Profile
from tastyRecipesApp.utils import get_profile


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, 'profiles/create-profile.html', context)


# class CreateProfileView(CreateView):
#     model = Profile
#     form_class = ProfileCreateForm
#     template_name = 'profiles/create-profile.html'
#     success_url = reverse_lazy('catalogue')


def show_details_profile(request):
    profile = get_profile()

    context = {'profile': profile}

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
        'profile': profile,
        'form': form
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    form = ProfileDeleteForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('home page')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profiles/delete-profile.html', context)
