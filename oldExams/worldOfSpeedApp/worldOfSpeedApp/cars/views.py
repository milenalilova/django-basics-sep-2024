from django.shortcuts import render, redirect

from worldOfSpeedApp.cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from worldOfSpeedApp.cars.models import Car
from worldOfSpeedApp.utils import get_profile


def show_car_catalogue(request):
    profile = get_profile()
    all_cars = Car.objects.all()

    context = {
        'all_cars': all_cars,
        'profile': profile
    }

    return render(request, 'cars/catalogue.html', context)


def create_car(request):
    profile = get_profile()
    form = CarCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = profile
            car.save()
            return redirect('catalogue')

    context = {'form': form,
               'profile': profile
               }

    return render(request, 'cars/car-create.html', context)


def show_car_details(request, id):
    profile = get_profile()
    car = Car.objects.get(id=id)

    context = {
        'car': car,
        'profile': profile
    }

    return render(request, 'cars/car-details.html', context)


def edit_car(request, id):
    profile = get_profile()
    car = Car.objects.get(id=id)
    form = CarEditForm(instance=car)

    if request.method == 'POST':
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': profile
    }

    return render(request, 'cars/car-edit.html', context)


def delete_car(request, id):
    profile = get_profile()
    car = Car.objects.get(id=id)
    form = CarDeleteForm(instance=car)

    if request.method == 'POST':
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            car.delete()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form
    }

    return render(request, 'cars/car-delete.html', context)
