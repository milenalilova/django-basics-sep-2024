from django import forms

from fruitipediaApp.profiles.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password',
                                                   'help_text': '*Password length requirements: 8 to 20 characters'}),
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()