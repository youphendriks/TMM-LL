from objects.database_client import db_client
from objects.repositories.deck_repository import deck_repository


# Get stats about a deck
def get_deckstats(deck_name):
    return deck_repository.get_deckstats(deck_name)
