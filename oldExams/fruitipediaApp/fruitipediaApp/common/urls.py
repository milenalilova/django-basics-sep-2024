from django.urls import path

from fruitipediaApp.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.show_dashboard, name='dashboard')
]
