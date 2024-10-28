from django import forms

from furryFunniesApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:'
        }


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        }


class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        help_texts = {'image_url': ''}


class PostDeleteForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        help_texts = {'image_url': ''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
