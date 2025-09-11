import pandas as pd
from pandas import DataFrame

from objects.database_client import db_client


class EntryRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.entry

    def add_entry(self, R, P1_id, D1_id, S1, P2_id, D2_id, S2, datetime):
        return self._collection.insert_one(
            {
                "round": R,
                "player1": P1_id,
                "deck1": D1_id,
                "score1": S1,
                "player2": P2_id,
                "deck2": D2_id,
                "score2": S2,
                "datetime": datetime,
            }
        )

    def get_entries(self):
        return self._collection.find()

    def get_entries_for_player(self, playername):
        query = {"$or": [{"player1": playername}, {"player2": playername}]}
        return self._collection.find(query)


entry_repository = EntryRepository()

