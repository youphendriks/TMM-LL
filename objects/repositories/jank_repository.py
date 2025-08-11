from objects.database_client import db_client

class JankRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.jank

    def add_jank_points_for_player(self, player_id, points, fnm_date):
        return self._collection.insert_one(
            {"playerid": player_id, "points": points, "fnmdate": fnm_date}
        )

    def get_all_jank(self):
        return self._collection.find()
    
    def get_jank_for_player(self, player_id):
        return self._collection.find({"playerid": player_id})

jank_repository = JankRepository()