from django.shortcuts import render, redirect

from employeesApp.departments.forms import DepartmentForm, DepartmentDeleteForm
from employeesApp.departments.models import Department


def show_departments_list(request):
    departments = Department.objects.all()

    context = {'departments': departments}

    return render(request, 'departments/departments-list.html', context)


def create_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departments list')

    context = {'form': form}

    return render(request, 'departments/create-department.html', context)


def delete_department(request, pk):
    department = Department.objects.get(pk=pk)
    delete_form = DepartmentDeleteForm()

    if request.method == 'POST':
        department.delete()
        return redirect('departments list')

    context = {
        'department': department,
        'delete_form': delete_form
    }

    return render(request, 'departments/delete-department.html', context)
