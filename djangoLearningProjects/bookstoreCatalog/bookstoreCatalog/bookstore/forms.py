from django import forms

from bookstoreCatalog.bookstore.models import Author


class NameForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
