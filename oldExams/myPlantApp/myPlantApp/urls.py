from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myPlantApp.common.urls')),
    path('', include('myPlantApp.plants.urls')),
    path('profile/', include('myPlantApp.profiles.urls'))
]
