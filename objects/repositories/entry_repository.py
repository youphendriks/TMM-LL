from objects.database_client import db_client


class EntryRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.entry

    def add_entry(self, R, P1, D1, S1, P2, D2, S2, D):
        return self._collection.insert_one(
            {
                "round": R,
                "player1": P1["playername"],
                "deck1": D1["deckname"],
                "score1": S1,
                "player2": P2["playername"],
                "deck2": D2["deckname"],
                "score2": S2,
                "datetime": D,
            }
        )

    def get_entries(self):
        return self._collection.find()

    def get_entries_for_deck(self, deck):
        query = {"$or": [{"deck1": deck}, {"deck2": deck}]}
        return self._collection.find(query)

    def get_entries_for_player(self, playername):
        query = {"$or": [{"player1": playername}, {"player2": playername}]}
        return self._collection.find(query)


entry_repository = EntryRepository()
