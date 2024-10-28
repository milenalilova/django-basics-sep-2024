from django import forms

from furryFunniesApp.authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        fields = ['first_name', 'last_name', 'passcode', 'pets_number']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pet Number:',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:',
        }


class AuthorDeleteForm(AuthorBaseForm):
    pass
