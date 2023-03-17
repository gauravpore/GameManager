from rest_framework import serializers
from core.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "game_id",
            "name",
            "url",
            "author",
            "published_date",
        )
