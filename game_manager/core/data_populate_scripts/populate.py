import pandas as pd

from core.models import Game

df = pd.read_csv(
    "C:/Users/poreg/OneDrive/Desktop/GameManager/game_manager/core/data_populate_scripts/test_data.csv"
)


def populate_games_data():
    """
    Populates Game model entries
    """
    for ind in range(0, 29):
        name = df["name"][ind]
        url = df["url"][ind]
        author = df["author"][ind]
        published_date = df["published_date"][ind]
        existing_game = Game.objects.filter(name=name).first()
        if existing_game:
            continue
        new_game = Game.objects.create(
            name=name, url=url, author=author, published_date=published_date
        )
        new_game.save()
    return True, "New Games test data created successfully!"
