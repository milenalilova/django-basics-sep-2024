from django import forms

from worldOfSpeedApp.profiles.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        # help_texts = {
        #     'age': 'Age requirement: 21 years and above.'
        # }
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
