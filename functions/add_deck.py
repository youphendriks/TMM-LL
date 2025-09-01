from objects.repositories.deck_repository import deck_repository

# Add deck to DB
def add_deck(deckname):
    return deck_repository.add_deck(deckname)
