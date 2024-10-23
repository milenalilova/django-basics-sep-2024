from django.shortcuts import render

from worldOfSpeedApp.utils import get_profile


def index(request):
    profile = get_profile()

    context = {'profile': profile}

    return render(request, 'common/index.html', context)
