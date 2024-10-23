from django.core import validators
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeedApp.profiles.validators import validate_username


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message='Username must be at least 3 chars long!'),
            validate_username],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(21)],
        help_text='Age requirement: 21 years and above.',
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return self.first_name
        if self.last_name:
            return self.last_name
        return None

    def total_car_price(self):
        total_price = self.car_set.aggregate(total_price=models.Sum('price'))['total_price'] or 0

        return total_price
