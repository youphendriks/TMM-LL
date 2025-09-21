from objects.database_client import db_client

class PollRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.polls

    def add_poll(self, poll):
        self._collection.insert_one(poll)


poll_repository = PollRepository()