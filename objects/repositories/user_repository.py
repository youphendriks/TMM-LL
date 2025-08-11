from objects.database_client import db_client

class UserRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.users

    def add_user(self, user):
        new_user = self._collection.insert_one(user)
        return new_user.inserted_id
    
    def get_user(self, id):
        return self._collection.find_one(id)
    
    def get_user_by_player_id(self, player_id):
        return self._collection.find_one({"playerid": player_id})

    def get_user_by_idp_id(self, idp_id):
        return self._collection.find_one({"idpid": idp_id})

user_repository = UserRepository()