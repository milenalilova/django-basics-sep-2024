from django.urls import path, include
from employeesApp.employees import views

urlpatterns = [
    path('', views.show_employees_list, name='employees list'),
    path('create/', views.create_employee, name='create employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete employee'),
]
