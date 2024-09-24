from django.urls import path

from templatesBasics.departments import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.show_departments_list, name='departments list'),
    path('departments/<int:pk>/', views.show_departments_details, name='department details'),
    path('employees/', views.show_employees_list, name='employees list'),
    path('employees/count/', views.show_employees_count_per_department, name='employees count per department'),
    path('bootstrap/', views.show_bootstrap, name='bootstrap'),

]
