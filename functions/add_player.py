from objects.repositories.player_repository import player_repository
from objects.repositories.rank_repository import rank_repository

# Add player to DB
def add_player(playername):
    player_id = player_repository.add_player(playername)
    rank_repository.add_ranking_for_player(player_id)
    return player_repository.get_player(player_id)
