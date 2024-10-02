from django.shortcuts import render, redirect
from django.db.models import Q

from formsBasics.employees.forms import EmployeeForm, EmployeeDeleteForm, EmployeeSearchForm, DepartmentForm, \
    SelectOptionForm, CheckboxForm, RadioButtonForm
from formsBasics.employees.models import Department, Employee


def index(request):
    select_option_form = SelectOptionForm()
    checkbox_form = CheckboxForm()
    radio_button_form = RadioButtonForm()

    context = {
        'select_option_form': select_option_form,
        'checkbox_form': checkbox_form,
        'radio_button_form': radio_button_form,
    }

    return render(request, 'employees/home-page.html', context)


def show_departments_list(request):
    return render(request, 'employees/departments-list.html')


def show_employees_list(request):
    employees = Employee.objects.all()
    employee_search_form = EmployeeSearchForm(request.GET or None)

    if employee_search_form.is_valid():
        query = employee_search_form.cleaned_data['query']
        if query:
            employees = employees.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )

    context = {
        'employees': employees,
        'employee_search_form': employee_search_form
    }

    return render(request, 'employees/employees-list.html', context)


def create_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departments list')

    context = {'form': form}

    return render(request, 'employees/create-department.html', context)


def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employees list')

    context = {'form': form}

    return render(request, 'employees/create-employee.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    delete_form = EmployeeDeleteForm(instance=employee)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees list')

    context = {
        'delete_form': delete_form,
        'employee': employee
    }

    return render(request, 'employees/delete-employee.html', context)
