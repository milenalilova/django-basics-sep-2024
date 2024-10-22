from django.urls import path

from tastyRecipesApp.profiles import views

urlpatterns = [
    path('create/', views.create_profile, name='create profile'),
    path('details/', views.show_details_profile, name='details profile'),
    path('edit/', views.edit_profile, name='edit profile'),
    path('detele/', views.delete_profile, name='delete profile'),
]
