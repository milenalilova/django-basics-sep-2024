from django.shortcuts import render

from formsBasics.employees.models import Department


def index(request):
    return render(request, 'employees/home-page.html')


def show_departments_list(request):
    return render(request, 'employees/departments-list.html')


def show_employees_list(request):
    return render(request, 'employees/employees-list.html')


def create_department(request):
    return render(request, 'employees/create-department.html')


def create_employee(request):
    return render(request, 'employees/create-employee.html')
