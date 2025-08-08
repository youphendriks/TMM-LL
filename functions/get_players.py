from objects.database_client import db_client
from objects.repositories.player_repository import player_repository


# # Pull playernames from players collection.
def get_players():
    return player_repository.get_players()
