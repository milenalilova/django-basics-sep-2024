from django.urls import path, include

from formsBasics import employees
from formsBasics.employees import views

urlpatterns = [
    path('', views.index, name='home page'),
    path('departments/', include([
        path('', views.show_departments_list, name='departments list'),
        path('create/', views.create_department, name='create department'),
    ])),
    path('employees/', include([
        path('', views.show_employees_list, name='employees list'),
        path('create/', views.create_employee, name='create employee'),
    ])),
]
