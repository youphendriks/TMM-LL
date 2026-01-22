import re

from objects.database_client import db_client


class DeckstatsRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.deck_stats

    def get_deckstats(self):
        return self._collection.find().to_list()

    def get_deckstats_for_deck(self, deck_name: str):
        deckstats = []
        return deckstats

    def add_deck(
        self,
        deck: str,
        game_win_percentage: int,
        games_count: int,
        match_count: int,
        match_win_percentage: int,
        games_win: int,
        match_win: int,
    ):
        # otherwise create deck
        return self._collection.insert_one(
            {
                "deck": deck,
                "game_win_percentage": game_win_percentage,
                "games_count": games_count,
                "match_count": match_count,
                "match_win_percentage": match_win_percentage,
                "games_win": games_win,
                "match_win": match_win,
            }
        )


deckstats_repository = DeckstatsRepository()
