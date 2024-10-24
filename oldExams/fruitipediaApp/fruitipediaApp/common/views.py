from django.shortcuts import render

from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.utils import get_profile


def index(request):
    profile = get_profile()

    context = {'profile': profile}

    return render(request, 'common/index.html', context)


def show_dashboard(request):
    profile = get_profile()
    all_fruits = Fruit.objects.all()

    context = {
        'all_fruits': all_fruits,
        'profile': profile
    }

    return render(request, 'common/dashboard.html', context)
