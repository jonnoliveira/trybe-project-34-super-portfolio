from django.core.exceptions import ValidationError


def count_char(param):
    if len(param) >= 500:
        raise ValidationError("Field cannot be this size.")
