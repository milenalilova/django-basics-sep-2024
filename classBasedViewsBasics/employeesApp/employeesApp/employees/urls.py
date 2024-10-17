from django.urls import path, include
from employeesApp.employees import views
from employeesApp.employees.views import CreateEmployee

urlpatterns = [
    path('', views.show_employees_list, name='employees list'),
    path('create/', CreateEmployee.as_view(), name='create employee'),
    path('details/<int:pk>/', views.show_employee_details, name='employee details'),
    path('<int:pk>/delete/', views.delete_employee, name='delete employee'),
]
