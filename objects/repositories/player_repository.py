from objects.database_client import db_client

class PlayerRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.players

    def get_players(self):
        return self._collection.find().to_list()
    
    def get_player(self, id):
        return self._collection.find_one(id)
    
    def add_player(self, player_name: str):
        item = self._collection.insert_one({"playername": player_name})
        return item.inserted_id
    
player_repository = PlayerRepository()
