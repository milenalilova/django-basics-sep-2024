from django.urls import path

from urlsAndViews.departments import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.show_departments_by_name, name='show departments by name'),
    path('departments/<int:pk>/', views.show_departments_by_id, name='show departments by id'),
]
