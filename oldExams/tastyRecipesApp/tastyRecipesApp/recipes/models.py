from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from tastyRecipesApp.profiles.models import Profile


class Recipe(models.Model):
    class CuisineTypeChoices(models.TextChoices):
        FRENCH = 'French', 'French'
        CHINESE = 'Chinese', 'Chinese'
        ITALIAN = 'Italian', 'Italian'
        BALKAN = 'Balkan', 'Balkan'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(10)],
        error_messages={
            'unique': 'We already have a recipe with the same title!'
        },
        null=False,
        blank=False,
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices.choices,
        null=False,
        blank=False,
    )

    ingredients = models.TextField(
        help_text='Ingredients must be separated by a comma and space.',
        null=False,
        blank=False,
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text='Provide the cooking time in minutes.',
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)


