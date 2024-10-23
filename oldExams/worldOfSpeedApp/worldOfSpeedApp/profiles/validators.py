from django.core.exceptions import ValidationError


def validate_username(username):
    if not all(ch.isalnum() or ch == '_' for ch in username):
        raise ValidationError('Username must contain only letters, digits, and underscores!')
