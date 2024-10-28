from django.core.validators import MinLengthValidator
from django.db import models

from furryFunniesApp.authors.models import Author


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        error_messages={
            'unique': 'Oops! That title is already taken. How about something fresh and fun?'
        },
        unique=True,
        null=False,
        blank=False
    )

    image_url = models.URLField(
        help_text='Share your funniest furry photo URL!',
        null=False,
        blank=False
    )

    content = models.TextField(
        null=False,
        blank=False
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
