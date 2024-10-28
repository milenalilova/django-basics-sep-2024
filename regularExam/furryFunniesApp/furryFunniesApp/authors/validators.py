from django.core.exceptions import ValidationError


def validate_name_only_letters(name):
    if not name.isalpha():
        raise ValidationError('Your name must contain letters only!')


def validate_passcode(passcode):
    if len(passcode) != 6 or not passcode.isdigit():
        raise ValidationError('Your passcode must be a combination of 6 digits')
