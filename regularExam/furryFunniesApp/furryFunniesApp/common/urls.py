from django.urls import path

from furryFunniesApp.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.show_dashboard, name='dashboard')
]
