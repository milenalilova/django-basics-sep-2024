from django.shortcuts import render

from tastyRecipesApp.utils import get_profile


def index(request):
    profile = get_profile()

    context = {'profile': profile}

    return render(request, 'common/home-page.html', context)
