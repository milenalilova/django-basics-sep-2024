from django.core.exceptions import ValidationError


def validate_name_contains_only_letters(name):
    if not all(ch.isalpha() for ch in name):
        raise ValidationError('Fruit name should contain only letters!')
