from django.urls import path, include

from worldOfSpeedApp import cars
from worldOfSpeedApp.cars.views import show_car_catalogue, create_car, show_car_details, edit_car, delete_car

urlpatterns = [
    path('catalogue/', show_car_catalogue, name='catalogue'),
    path('create/', create_car, name='create car'),
    path('<int:id>/', include([
        path('details/', show_car_details, name='details car'),
        path('edit/', edit_car, name='edit car'),
        path('delete/', delete_car, name='delete car'),
    ])),
]
