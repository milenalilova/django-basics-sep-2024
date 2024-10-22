from django.urls import path, include

from myMusicApp.albums import views

urlpatterns = (
    path('add/', views.AddAlbumView.as_view(), name='add album'),
    path('<int:pk>/',
         include([
             path('details/', views.AlbumDetailView.as_view(), name='details album'),
             path('edit/', views.AlbumEditView.as_view(), name='edit album'),
             path('delete/', views.AlbumDeleteView.as_view(), name='delete album'),
         ])
         )
)
