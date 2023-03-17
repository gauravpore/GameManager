from django.contrib import admin

from .models import Game
from django.contrib.admin import ModelAdmin

# Register your models here.
class GameUserAdmin(ModelAdmin):
    search_fields = (
        "game_id",
        "name",
    )
    list_display = (
        "game_id",
        "name",
        "url",
        "author",
        "published_date",
        "created_date",
        "updated_date",
    )


admin.site.register(Game, GameUserAdmin)
