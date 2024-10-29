from django.urls import path

from furryFunniesApp.common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard')
]
