from objects.database_client import db_client
from objects.repositories.entry_repository import entry_repository


# Add score to the entry collection.
def add_data(R, P1, D1, S1, P2, D2, S2, datetime):
    return entry_repository.add_entry(
        R, P1["_id"], D1["_id"], S1, P2["_id"], D2["_id"], S2, datetime
    )
