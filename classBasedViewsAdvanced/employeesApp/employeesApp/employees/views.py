from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from employeesApp.employees.forms import EmployeeForm, EmployeeDeleteForm, EmployeeSearchForm, EmployeeFeedbackForm
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


from django.views import View

class EmployeeDetails(DetailView):
    model = Employee
    template_name = 'employees/employee-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback_form'] = EmployeeFeedbackForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = EmployeeFeedbackForm(request.POST)

        print("Post method called")
        print("Form data:", request.POST)

        if form.is_valid():
            print("Form is valid.")
            print("Cleaned data:", form.cleaned_data)
            messages.success(request, 'Thank you for your feedback!')
            return self.get(request, *args, **kwargs)  # Redirect back to the detail view

        # TODO add redirect after feedback submitted

        else:
            print("Form is invalid.")
            print("Errors:", form.errors)
            messages.error(request, 'There were errors in your submission. Please correct them.')
            context = self.get_context_data(feedback_form=form)  # Pass the form with errors
            return self.render_to_response(context)



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
