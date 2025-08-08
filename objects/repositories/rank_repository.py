from objects.database_client import db_client

class RankRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.rankings

    def add_ranking_for_player(self, player_id):
        self._collection.insert_one({"playerid": player_id, "score": 0})

    #def update_ranking_for_player(self, player_id):


rank_repository = RankRepository()