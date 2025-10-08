from objects.database_client import db_client


class EntryRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.entry

    def add_entry(self, R, P1, D1, S1, P2, D2, S2, D):
        return self._collection.insert_one(
            {
                "round": R,
                "player1": P1,
                "deck1": D1,
                "score1": S1,
                "player2": P2,
                "deck2": D2,
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

    def get_total_games(self):
        pipeline = [
            {
                "$project": {
                    "score1": "$score1",
                    "score2": "$score2",
                    "totalSum": {"$add": ["$score1", "$score2"]},
                }
            }
        ]
        entries = self._collection.aggregate(pipeline)
        total_games = 0
        for entry in entries:
            total_games += entry["totalSum"]
        return total_games

    def get_total_matches(self):
        # entries = self._collection.find()
        total_matches = self._collection.count_documents({})
        return total_matches


entry_repository = EntryRepository()
