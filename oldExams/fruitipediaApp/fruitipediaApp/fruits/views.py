from django.shortcuts import render, redirect

from fruitipediaApp.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.utils import get_profile


def create_fruit(request):
    profile = get_profile()
    form = FruitCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            fruit = form.save(commit=False)
            fruit.owner_id = profile.pk
            fruit.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'fruits/create-fruit.html', context)


def show_details_fruit(request, fruit_id):
    profile = get_profile()
    fruit = Fruit.objects.get(pk=fruit_id)

    context = {
        'fruit': fruit,
        'profile': profile
    }

    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_id):
    profile = get_profile()
    fruit = Fruit.objects.get(pk=fruit_id)
    form = FruitEditForm(instance=fruit)

    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'profile': profile,
        'form': form
    }

    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    profile = get_profile()
    fruit = Fruit.objects.get(pk=fruit_id)
    form = FruitDeleteForm(instance=fruit)

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'fruits/delete-fruit.html', context)
