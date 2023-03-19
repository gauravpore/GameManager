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


class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["name", "url", "author", "published_date"]


class UpdateGameSerializer(serializers.Serializer):
    game_id = serializers.CharField()
    name = serializers.CharField(required=False)
    url = serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    published_date = serializers.DateField(required=False)
