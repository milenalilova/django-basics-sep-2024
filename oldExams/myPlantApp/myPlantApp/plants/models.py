from django.core.validators import MinLengthValidator
from django.db import models

from myPlantApp.plants.validators import validate_name_contains_only_letters


class Plant(models.Model):
    class PlantTypes(models.TextChoices):
        OUTDOOR_PLANT = 'Outdoor Plants', 'Outdoor Plants'
        INDOOR_PLANTS = 'Indoor Plants', 'Indoor Plants'

    plant_type = models.CharField(
        max_length=14,
        choices=PlantTypes.choices,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(2),
            validate_name_contains_only_letters
        ],
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

    price = models.FloatField(
        null=False,
        blank=False
    )
