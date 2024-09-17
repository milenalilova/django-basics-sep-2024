from django.contrib import admin
from django.urls import path, include

import djangoIntroduction.tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoIntroduction.tasks.urls')),
]
