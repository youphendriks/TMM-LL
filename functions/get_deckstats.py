from objects.database_client import db_client
from objects.repositories.deckstats_repository import deckstats_repository


# Get stats about a deck
def get_deckstats():
    return deckstats_repository.get_deckstats()


# Get stats about a deck
def get_deckstats_for_deck(deck_name):
    return deckstats_repository.get_deckstats_for_deck(deck_name)
