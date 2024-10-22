from django.urls import path

from tastyRecipesApp.common.views import index

urlpatterns = [
    path('', index, name='home page'),
]
