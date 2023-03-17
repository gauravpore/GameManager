from django.urls import path

from .views import GameController


urlpatterns = [
    path("create-game", GameController.create_single_game, name="create-new-game"),
    path("read-game", GameController.read_single_game, name="read-single-game"),
    path("get-all-games", GameController.get_all_games, name="get-all-games"),
    path("update-game", GameController.update_single_game, name="update-single-game"),
    path("delete-game", GameController.delete_single_game, name="delete-single-game"),
]
