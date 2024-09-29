from django import forms

from formsBasics.employees.models import Employee, Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
