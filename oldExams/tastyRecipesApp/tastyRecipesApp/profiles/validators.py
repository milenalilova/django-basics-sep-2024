from django.core.exceptions import ValidationError


def validate_name_capitalized(name):
    if not name[0].isupper():
        raise ValidationError('Name must start with a capital letter!')
