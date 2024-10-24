from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import validate_name_contains_only_letters
from fruitipediaApp.profiles.models import Profile


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            validate_name_contains_only_letters
        ],
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.'
        },
        unique=True,
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    nutrition = models.TextField(
        null=True,
        blank=True
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

#     TODO owner to be hidden in forms
