import re

from objects.database_client import db_client


class DeckRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.decks

    def get_deck(self, deck_id):
        return self._collection.find_one(deck_id)

    def get_decks(self):
        return self._collection.find().to_list()

    def get_deck_by_name(self, deck_name: str):
        return self._collection.find_one(
            {"deckname": re.compile(f"^{deck_name}$", re.IGNORECASE)}
        )

    def add_deck(self, deck_name: str):
        # first check if deck already exists
        existing_deck = self.get_deck_by_name(deck_name)

        # return existing deck
        if existing_deck:
            return existing_deck

        # otherwise create deck
        return self._collection.insert_one({"deckname": deck_name})

    def get_deckstats(self):
        deckstats = []
        return deckstats

    def get_deckstats_for_deck(self, deck_name: str):
        deckstats = []
        return deckstats


deck_repository = DeckRepository()
