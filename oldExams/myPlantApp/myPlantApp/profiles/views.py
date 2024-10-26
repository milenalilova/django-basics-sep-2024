from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView

from myPlantApp.plants.models import Plant
from myPlantApp.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from myPlantApp.profiles.models import Profile
from myPlantApp.utils import get_profile


# def create_profile(request):
#     form = ProfileCreateForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('catalogue')
#
#     context = {'form': form}
#
#     return render(request, 'profiles/create-profile.html', context)

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        return super().form_valid(form)


# def show_details_profile(request):
#     profile = get_profile()
#     all_plants = len(Plant.objects.all())
#
#     context = {
#         'profile': profile,
#         'all_plants': all_plants
#     }
#
#     return render(request, 'profiles/profile-details.html', context)


class ProfileDetailsView(TemplateView):
    template_name = 'profiles/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        context['all_plants'] = len(Plant.objects.all())
        return context


# def edit_profile(request):
#     profile = get_profile()
#     form = ProfileEditForm(request.POST or None, instance=profile)
#
#     if request.method == 'POST':
#         form = ProfileEditForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('details profile')
#
#     context = {
#         'form': form,
#         'profile': profile
#     }
#
#     return render(request, 'profiles/edit-profile.html', context)


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        return get_profile()


# def delete_profile(request):
#     profile = get_profile()
#     all_plants = Plant.objects.all()
#
#     form = ProfileDeleteForm(request.POST or None)
#
#     if request.method == 'POST':
#         profile.delete()
#         all_plants.delete()
#         return redirect('home page')
#
#     context = {
#         'form': form,
#         'profile': profile,
#         'all_plants': all_plants
#     }
#
#     return render(request, 'profiles/delete-profile.html', context)


class ProfileDeleteView(DeleteView):
    model = Profile
    form_class = ProfileDeleteForm
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('home page')

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_plants'] = Plant.objects.all()
        return context

    def form_valid(self, form):
        profile = self.get_object()
        Plant.objects.all().delete()
        profile.delete()
        return redirect(self.success_url)
