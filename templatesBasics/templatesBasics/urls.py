from django.contrib import admin
from django.urls import path, include

from templatesBasics.departments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('templatesBasics.departments.urls')),
]
