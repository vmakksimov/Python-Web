from django.core import exceptions
from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha() and not ch.isdigit() and not ch == '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")