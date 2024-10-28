from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('furryFunniesApp.common.urls')),
    path('author/', include('furryFunniesApp.authors.urls')),
    path('posts/', include('furryFunniesApp.posts.urls')),
]
