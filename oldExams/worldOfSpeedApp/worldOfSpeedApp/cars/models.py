from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeedApp.cars.validators import validate_year_in_range
from worldOfSpeedApp.profiles.models import Profile


class Car(models.Model):
    class TypeChoices(models.TextChoices):
        RALLY = 'Rally', 'Rally'
        OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
        KART = 'Kart', 'Kart'
        DRAG = 'Drag', 'Drag'
        OTHER = 'Other', 'Other'

    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        null=False,
        blank=False
    )

    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1)],
        null=False,
        blank=False
    )

    year = models.IntegerField(
        validators=[validate_year_in_range],
        null=False,
        blank=False
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        verbose_name='Image URL',
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.'
        }
    )

    price = models.FloatField(
        validators=[MinValueValidator(1.0)],
        null=False,
        blank=False
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)


