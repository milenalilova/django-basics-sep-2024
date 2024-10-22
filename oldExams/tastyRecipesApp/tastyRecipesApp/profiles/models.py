from django.core.validators import MinLengthValidator
from django.db import models

from tastyRecipesApp.profiles.validators import validate_name_capitalized


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2, message='Nickname must be at least 2 chars long!')],
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        validators=[validate_name_capitalized],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=30,
        validators=[validate_name_capitalized],
        null=False,
        blank=False,
    )

    chef = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    bio = models.TextField(
        null=True,
        blank=True
    )
