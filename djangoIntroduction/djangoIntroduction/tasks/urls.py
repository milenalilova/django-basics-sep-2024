from django.urls import path

from djangoIntroduction.tasks import views

urlpatterns = [
    path('', views.index),
]
