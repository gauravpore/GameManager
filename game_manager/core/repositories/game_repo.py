from core.models import Game
from core.serializers.game_serializer import GameSerializer


def create_game(game_data: dict):
    """
    Creates a single game object which does not exists in db.
    Params:
        - game_data -> Dict with all the required fields data
    Returns:
        success , response
    """
    name = game_data.get("name")
    existing_game = Game.objects.filter(name=name)
    if existing_game:
        return False, "Game with given name already exists!"
    game_object = Game.objects.create(**game_data)
    game_object.save()
    return True, "Game object created successfully"


def read_game(name: str = None, game_id: str = None):
    """
    Retrieves a single game object from db based on game_id or name.
    Params:
        - name -> name of game
        - game_id -> id of game
    Returns:
        success , response
    """
    if not name and not game_id:
        return False, "Either game_id or name is required"
    if name:
        game_object = Game.objects.filter(name=name)
        if not game_object:
            return False, "Game not found with provided name"
    if game_id:
        game_object = Game.objects.filter(game_id=game_id)
        if not game_object:
            return False, "Game not found with provided game_id"
    serialized_data = GameSerializer(game_object[0]).data
    return True, serialized_data


def get_games():
    """
    Retrieves all games from db.
    Returns:
        success , response
    """
    all_games_objects = Game.objects.all()
    if not all_games_objects:
        return False, "No Games Found"
    serialized_data = GameSerializer(all_games_objects, many=True).data
    return True, serialized_data


def update_game(game_id: str, game_data: dict):
    """
    Updates the provided game data for game with matching game_id.
    Params:
        - game_id -> id of game
        - game_data -> game data that needs to be updated
    Returns:
        success , response
    """
    game_object = Game.objects.filter(game_id=game_id).first()
    if not game_object:
        return False, "Game not found with provided game_id"
    for k, v in game_data.items():
        setattr(game_object, k.lower(), v)
    game_object.save()
    return True, "Game data Updated Successfully"


def delete_game(name: str = None, game_id: str = None):
    """
    Deletes the game object with matching game_id.
    Params:
        - name -> name of game
        - game_id -> id of game
    Returns:
        success , response
    """
    if not name and not game_id:
        return False, "Either game_id or name is required"
    if name:
        game_object = Game.objects.filter(name=name)
        if not game_object:
            return False, "Game not found with provided name"
    if game_id:
        game_object = Game.objects.filter(game_id=game_id)
        if not game_object:
            return False, "Game not found with provided game_id"
    game_object.delete()
    return True, "Requested Game deleted successfully"
