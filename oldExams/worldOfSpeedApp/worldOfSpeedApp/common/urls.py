from django.urls import path

from worldOfSpeedApp.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
