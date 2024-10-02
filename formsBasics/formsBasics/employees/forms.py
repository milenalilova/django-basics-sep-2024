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


class EmployeeDeleteForm(EmployeeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class EmployeeSearchForm(forms.Form):
    query = forms.CharField(label='Search Employees', max_length=100, required=False)


class SelectOptionForm(forms.Form):
    CHOICES = (
        ('1', 'Option One'),
        ('2', 'Option Two'),
    )

    choice_field = forms.ChoiceField(choices=CHOICES)
    char_field = forms.CharField(widget=forms.Select(choices=CHOICES))


class CheckboxForm(forms.Form):
    checkbox_field = forms.BooleanField(required=False)


class RadioButtonForm(forms.Form):
    CHOICES = (
        ('1', 'Option One'),
        ('2', 'Option Two'),
    )

    choices_field = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(),
    )

    char_field = forms.CharField(
        widget=forms.RadioSelect(
            choices=CHOICES
        )
    )
