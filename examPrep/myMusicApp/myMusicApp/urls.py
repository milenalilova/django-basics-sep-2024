from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myMusicApp.common.urls')),
    path('album/', include('myMusicApp.albums.urls')),
    path('profile/', include('myMusicApp.profiles.urls')),
]
