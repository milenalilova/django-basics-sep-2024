from django.urls import path, include

from employeesApp.departments import views

urlpatterns = [
    path('', views.show_departments_list, name='departments list'),
    path('create/', views.create_department, name='create department'),
    path('<int:pk>/details/', views.department_details, name='department details'),
    path('<int:pk>/delete/', views.delete_department, name='delete department'),
]
