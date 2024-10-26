from django.urls import path

from myPlantApp.plants import views

urlpatterns = [
    path('catalogue/', views.CatalogueView.as_view(), name='catalogue'),
    path('create/', views.PlantCreateView.as_view(), name='create plant'),
    path('details/<int:plant_id>/', views.PlantDetailView.as_view(), name='details plant'),
    path('edit/<int:plant_id>/', views.PlantEditView.as_view(), name='edit plant'),
    path('delete/<int:plant_id>/', views.PlantDeleteView.as_view(), name='delete plant'),
]
