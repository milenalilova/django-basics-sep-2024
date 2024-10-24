from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.profiles.validators import validate_name_starts_with_letter


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            validate_name_starts_with_letter],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            validate_name_starts_with_letter
        ],
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=40,
        unique=True,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8)
        ],
        help_text='*Password length requirements: 8 to 20 characters',
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    age = models.PositiveIntegerField(
        default=18,
        null=True,
        blank=True
    )




