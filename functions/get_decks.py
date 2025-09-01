from objects.repositories.deck_repository import deck_repository

# Pull decks from decks collection.
def get_decks():
    return deck_repository.get_decks()
