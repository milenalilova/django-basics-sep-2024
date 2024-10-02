from django import forms

from employeesApp.departments.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeDeleteForm(EmployeeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class EmployeeSearchForm(forms.Form):
    query = forms.CharField(label='Search Employees', max_length=100, required=False)
