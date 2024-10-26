from django.urls import path

from myPlantApp.profiles import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='create profile'),
    path('details/', views.show_details_profile, name='details profile'),
    path('edit/', views.ProfileEditView.as_view(), name='edit profile'),
    path('delete/', views.delete_profile, name='delete profile'),
]
