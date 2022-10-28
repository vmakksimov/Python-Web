from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from Music_app_prepExam.web.validators import only_letters_validator


# Create your models here.
class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    AGE_MIN = 0


    USERNAME_MAX_LENGTH = 15


    BUDGET_MIN_VALUE = 0
    BUDGET_DEFAULT_VALUE = 0
    IMAGE_UPLOAD_TO_DIR = 'profiles/'
    IMAGE_MAX_SIZE_IN_MB = 5

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
        )


    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN),
        )

    )

class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0.0

    POP = 'Pop Music'
    JAZZ = 'Jazz Music'
    RB = 'R&B Music'
    ROCK = 'Rock Music'
    COUNTRY = 'Country Music'
    DANCE = 'Dance Music'
    HIPANDHOP = 'Hip Hop Music'
    OTHER = 'Other'
    TYPES = [(x, x) for x in (POP, JAZZ, RB, ROCK, COUNTRY, DANCE, HIPANDHOP, OTHER)]

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH,
        #DA NAPRAVQ UNIQUE TOGETHER
    )

    artist_name = models.CharField(
        null=False,
        blank=False,
        max_length=ARTIST_NAME_MAX_LENGTH,
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=GENRE_MAX_LENGTH,
        choices=TYPES,
    )

    description = models.TextField(
        null=True,
        blank=True,

    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )


    )




