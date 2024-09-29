from django.shortcuts import render, redirect

from formsBasics.employees.forms import EmployeeForm, DepartmentForm
from formsBasics.employees.models import Department


def index(request):
    return render(request, 'employees/home-page.html')


def show_departments_list(request):
    return render(request, 'employees/departments-list.html')


def show_employees_list(request):
    return render(request, 'employees/employees-list.html')


def create_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departments list')

    context = {'form': form}

    return render(request, 'employees/create-department.html', context)


def create_employee(request):
    form = EmployeeForm()
    context = {'form': form}

    return render(request, 'employees/create-employee.html', context)
