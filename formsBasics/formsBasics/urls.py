from django.contrib import admin
from django.urls import path, include

from formsBasics import employees

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formsBasics.employees.urls')),
]
