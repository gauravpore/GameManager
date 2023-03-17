import random

# Create your models here.
from django.db.models import (
    Model,
    CharField,
    URLField,
    DateField,
)
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


def generate_game_id(char_len=5):
    game_id = "".join(
        [random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ") for i in range(char_len)]
    )
    return game_id


class Game(Model):
    """
    Model to store all Games with respective details
    """

    game_id = CharField(max_length=5, default=generate_game_id, unique=True)
    name = CharField(max_length=100, unique=True)
    url = URLField(max_length=100)
    author = CharField(max_length=100)
    published_date = DateField()
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    def __str__(self):
        return f"{self.name}"
