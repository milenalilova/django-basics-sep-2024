from django import forms

from fruitipediaApp.fruits.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class FruitDeleteForm(FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        exclude = ['nutrition']
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
