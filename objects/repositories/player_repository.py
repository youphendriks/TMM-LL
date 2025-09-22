import re

from objects.database_client import db_client


class PlayerRepository:
    def __init__(self):
        self._collection = db_client.get_client().TMMDB.players

    def get_player(self, id):
        return self._collection.find_one(id)

    def get_players(self):
        return self._collection.find().to_list()

    def get_player_by_name(self, given_name, email):

        matches = list(
            self._collection.find(
                {
                    "playername": re.compile(
                        f".*{re.escape(given_name)}.*", re.IGNORECASE
                    )
                }
            )
        )

        if not matches:
            return None  # No matches by given_name

        if len(matches) == 1:
            return matches[0]  # Only one match by first name

        # Multiple matches, now filter those whose playername also contains family_name
        for player in matches:
            if player.get("playername", "").lower() in email.lower():
                return player

        # No match found containing both names
        return None

    def add_player(self, player_name: str):
        item = self._collection.insert_one({"playername": player_name})
        return item.inserted_id


player_repository = PlayerRepository()
