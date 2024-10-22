from django.urls import path, include

from tastyRecipesApp import recipes
from tastyRecipesApp.recipes import views

urlpatterns = [
    path('catalogue/', views.show_catalogue, name='catalogue'),
    path('create/', views.create_recipe, name='create recipe'),
    path('<int:recipe_id>/', include([
        path('details/', views.show_details_recipe, name='details recipe'),
        path('edit/', views.edit_recipe, name='edit recipe'),
        path('delete/', views.delete_recipe, name='delete recipe'),
    ])
         ),
]
