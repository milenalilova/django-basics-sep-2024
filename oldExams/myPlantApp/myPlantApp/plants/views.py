from django.shortcuts import render, redirect

from myPlantApp.plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from myPlantApp.plants.models import Plant
from myPlantApp.utils import get_profile


def show_catalog(request):
    profile = get_profile()
    all_plants = Plant.objects.all()

    context = {
        'all_plants': all_plants,
        'profile': profile
    }

    return render(request, 'plants/catalogue.html', context)


def create_plant(request):
    form = PlantCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, 'plants/create-plant.html', context)


def show_details_plant(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)

    context = {'plant': plant}

    return render(request, 'plants/plant-details.html', context)


def edit_plant(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    form = PlantEditForm(instance=plant)

    if request.method == 'POST':
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'plant': plant,
        'form': form
    }

    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, plant_id):
    plant = Plant.objects.get(pk=plant_id)
    form = PlantDeleteForm(instance=plant)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    context = {
        'plant': plant,
        'form': form
    }

    return render(request, 'plants/delete-plant.html', context)
