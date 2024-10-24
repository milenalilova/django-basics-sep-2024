from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruitipediaApp.common.urls')),
    path('fruit/', include('fruitipediaApp.fruits.urls')),
    path('profile/', include('fruitipediaApp.profiles.urls')),
]
