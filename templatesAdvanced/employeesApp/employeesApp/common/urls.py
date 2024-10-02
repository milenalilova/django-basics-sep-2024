from django.urls import path, include

from employeesApp.common import views

urlpatterns = [
    path('', views.index, name='home page'),
]
