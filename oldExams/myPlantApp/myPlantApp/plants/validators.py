from django.core.exceptions import ValidationError


def validate_name_contains_only_letters(name):
    if not name.isalpha():
        raise ValidationError('Plant name should contain only letters!')