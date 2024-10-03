from django.db.models import Q
from django.shortcuts import render, redirect

from employeesApp.employees.forms import EmployeeForm, EmployeeDeleteForm, EmployeeSearchForm
from employeesApp.employees.models import Employee


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
        'employee_search_form': employee_search_form,
    }

    return render(request, 'employees/employees-list.html', context)


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
    return render(request, 'employees/delete_employee.html', context)
