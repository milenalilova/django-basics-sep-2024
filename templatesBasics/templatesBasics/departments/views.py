from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from templatesBasics.departments.models import Department, Employee


def index(request):
    return render(request, 'departments/index.html')


def show_departments_list(request):
    departments = Department.objects.all()

    context = {'departments': departments}

    return render(request, 'departments/departments_list.html', context)


def show_departments_details(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = Employee.objects.filter(department=department)

    context = {
        'department': department,
        'employees': employees
    }

    return render(request, 'departments/departments_details.html', context)


def show_employees_list(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'departments/employees_list.html', context)


def show_employees_count_per_department(request):
    departments = Department.objects.all()
    departments_data = []
    for department in departments:
        employees_count = Employee.objects.filter(department=department).count()
        departments_data.append({'department': department, 'employees_count': employees_count})

    context = {'departments_data': departments_data}

    return render(request, 'departments/employees_count_per_department.html', context)


def show_bootstrap(request):
    return render(request, 'departments/bootstrap.html')git
