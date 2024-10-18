from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from employeesApp.departments.forms import DepartmentForm, DepartmentDeleteForm
from employeesApp.departments.models import Department


def show_departments_list(request):
    departments = Department.objects.all()

    context = {'departments': departments}

    return render(request, 'departments/departments-list.html', context)


def department_details(request, pk):
    department = get_object_or_404(Department, pk=pk)
    context = {'department': department}

    return render(request, 'departments/department-details.html', context)


class CreateDepartment(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/create-department.html'
    success_url = reverse_lazy('departments list')


class EditDepartment(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/edit-department.html'
    success_url = reverse_lazy('departments list')


class DeleteDepartment(DeleteView):
    model = Department
    form_class = DepartmentDeleteForm
    template_name = 'departments/delete-department.html'
    success_url = reverse_lazy('departments list')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        department = Department.objects.get(pk=pk)
        return department.__dict__
