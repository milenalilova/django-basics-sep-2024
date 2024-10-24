from django.core.exceptions import ValidationError


def validate_name_starts_with_letter(name):
    if not name[0].isalpha():
        raise ValidationError('Your name must start with a letter!')
