from django.urls import path

from furryFunniesApp.authors import views

urlpatterns = [
    path('create/', views.create_author, name='create author'),
    path('details/', views.show_details_author, name='details author'),
    path('edit/', views.edit_author, name='edit author'),
    path('delete/', views.delete_author, name='delete author')
]
