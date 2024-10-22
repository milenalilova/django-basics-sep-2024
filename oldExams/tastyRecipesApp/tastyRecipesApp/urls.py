from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tastyRecipesApp.common.urls')),
    path('profile/', include('tastyRecipesApp.profiles.urls')),
    path('recipe/', include('tastyRecipesApp.recipes.urls'))
]
