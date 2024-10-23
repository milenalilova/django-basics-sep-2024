from django.urls import path, include

from worldOfSpeedApp.profiles.views import create_profile,show_profile_details, edit_profile, delete_profile

urlpatterns = [
    path('create/', create_profile, name='create profile'),
    path('details/', show_profile_details, name='details profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]
