from django.urls import path

from myPlantApp.plants import views

urlpatterns = [
    path('catalogue/', views.show_catalog, name='catalogue'),
    path('create/', views.create_plant, name='create plant'),
    path('details/<int:plant_id>/', views.show_details_plant, name='details plant'),
    path('edit/<int:plant_id>/', views.edit_plant, name='edit plant'),
    path('delete/<int:plant_id>/', views.delete_plant, name='delete plant'),
]
