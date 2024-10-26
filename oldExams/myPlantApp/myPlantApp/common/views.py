from django.shortcuts import render
from django.views.generic import TemplateView

from myPlantApp.utils import get_profile


# def index(request):
#     profile = get_profile()
#
#     context = {'profile': profile}
#
#     return render(request, 'common/home-page.html', context)


class HomePageView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context
