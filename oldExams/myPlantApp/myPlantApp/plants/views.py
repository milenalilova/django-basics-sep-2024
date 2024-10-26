from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from myPlantApp.plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from myPlantApp.plants.models import Plant
from myPlantApp.utils import get_profile


# def show_catalog(request):
#     profile = get_profile()
#     all_plants = Plant.objects.all()
#
#     context = {
#         'all_plants': all_plants,
#         'profile': profile
#     }
#
#     return render(request, 'plants/catalogue.html', context)

class CatalogueView(ListView):
    model = Plant
    template_name = 'plants/catalogue.html'
    context_object_name = 'all_plants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


# def create_plant(request):
#     form = PlantCreateForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('catalogue')
#
#     context = {'form': form}
#
#     return render(request, 'plants/create-plant.html', context)


class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plants/create-plant.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        return super().form_valid(form)


# def show_details_plant(request, plant_id):
#     plant = Plant.objects.get(pk=plant_id)
#
#     context = {'plant': plant}
#
#     return render(request, 'plants/plant-details.html', context)

class PlantDetailView(DetailView):
    model = Plant
    template_name = 'plants/plant-details.html'
    context_object_name = 'plant'
    pk_url_kwarg = 'plant_id'


# def edit_plant(request, plant_id):
#     plant = Plant.objects.get(pk=plant_id)
#     form = PlantEditForm(instance=plant)
#
#     if request.method == 'POST':
#         form = PlantEditForm(request.POST, instance=plant)
#         if form.is_valid():
#             form.save()
#             return redirect('catalogue')
#
#     context = {
#         'plant': plant,
#         'form': form
#     }
#
#     return render(request, 'plants/edit-plant.html', context)

class PlantEditView(UpdateView):
    model = Plant
    form_class = PlantEditForm
    template_name = 'plants/edit-plant.html'
    success_url = reverse_lazy('catalogue')
    context_object_name = 'plant'
    pk_url_kwarg = 'plant_id'

    def get_object(self, queryset=None):
        return super().get_object(queryset)


# def delete_plant(request, plant_id):
#     plant = Plant.objects.get(pk=plant_id)
#     form = PlantDeleteForm(instance=plant)
#
#     if request.method == 'POST':
#         plant.delete()
#         return redirect('catalogue')
#
#     context = {
#         'plant': plant,
#         'form': form
#     }
#
#     return render(request, 'plants/delete-plant.html', context)


class PlantDeleteView(DeleteView):
    model = Plant
    form_class = PlantDeleteForm
    template_name = 'plants/delete-plant.html'
    success_url = reverse_lazy('catalogue')
    context_object_name = 'plant'
    pk_url_kwarg = 'plant_id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)



# TODO verify if the following code works
# class PlantDeleteView(DeleteView):
#     model = Plant
#     template_name = 'plants/delete-plant.html'
#     success_url = reverse_lazy('catalogue')
#     context_object_name = 'plant'
#     pk_url_kwarg = 'plant_id'
#
#     def get_form(self, form_class=None):
#         # Get the form instance with the plant instance
#         form = super().get_form(form_class)
#         # Assign the plant instance to the form
#         form.instance = self.get_object()
#         return form
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Add the prefilled form to the context
#         context['form'] = PlantDeleteForm(instance=self.get_object())
#         return context
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()  # Get the object to delete
#         self.object.delete()  # Delete the object
#         return self.get_success_response()

