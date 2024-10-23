from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('worldOfSpeedApp.common.urls')),
    path('car/', include('worldOfSpeedApp.cars.urls')),
    path('profile/', include('worldOfSpeedApp.profiles.urls')),
]
