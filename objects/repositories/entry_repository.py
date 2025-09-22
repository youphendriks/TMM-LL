from objects.database_client import db_client


class EntryRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.entry

    def add_entry(self, D, R, P1_id, D1_id, S1, P2_id, D2_id, S2):
        return self._collection.insert_one(
            {
                "datetime": D,
                "round": R,
                "player1": P1_id,
                "deck1": D1_id,
                "score1": S1,
                "player2": P2_id,
                "deck2": D2_id,
                "score2": S2,
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
