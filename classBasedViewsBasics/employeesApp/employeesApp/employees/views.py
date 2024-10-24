from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

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


def show_employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    context = {'employee': employee}

    return render(request, 'employees/employee-details.html', context)


# def create_employee(request):
#     form = EmployeeForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('employees list')
#
#     context = {'form': form}
#
#     return render(request, 'employees/create-employee.html', context)

class CreateEmployee(CreateView):
    fields = '__all__'
    model = Employee
    template_name = 'employees/create-employee.html'
    success_url = reverse_lazy('employees list')


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