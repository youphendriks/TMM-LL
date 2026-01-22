from objects.database_client import db_client
from objects.repositories.deckstats_repository import deckstats_repository


# Add score to the entry collection.
def add_deckstats(
    deck: str,
    game_win_percentage: int,
    games_count: int,
    match_count: int,
    match_win_percentage: int,
    games_win: int,
    match_win: int,
):

    return deckstats_repository.add_deckstats(
        deck,
        game_win_percentage,
        games_count,
        match_count,
        match_win_percentage,
        games_win,
        match_win,
    )
