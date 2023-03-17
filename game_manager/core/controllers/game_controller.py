from rest_framework.decorators import api_view
from core.repositories.game_repo import (
    create_game,
    read_game,
    get_games,
    update_game,
    delete_game,
)
from core.helpers.base import (
    SuccessJSONResponse,
    BadRequestJSONResponse,
)


class GameController:
    @staticmethod
    @api_view(["POST"])
    def create_single_game(request):
        post_data = request.data
        if (
            not post_data.get("name")
            or not post_data.get("url")
            or not post_data.get("author")
            or not ("published_date")
        ):
            return BadRequestJSONResponse(
                message="Inavlid request data. One or more params are missing!"
            )
        success, response = create_game(game_data=post_data)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["GET"])
    def read_single_game(request):
        game_id = request.GET.get("game_id")
        name = request.GET.get("name")
        success, response = read_game(name=name, game_id=game_id)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["GET"])
    def get_all_games(request):
        success, response = get_games()
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["PUT"])
    def update_single_game(request):
        post_data = request.data
        game_id = post_data.get("game_id")
        success, response = update_game(game_id=game_id, game_data=post_data)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["DELETE"])
    def delete_single_game(request):
        game_id = request.GET.get("game_id")
        name = request.GET.get("name")
        success, response = delete_game(name=name, game_id=game_id)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)
