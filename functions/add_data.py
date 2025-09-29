from objects.database_client import db_client
from objects.repositories.entry_repository import entry_repository


# Add score to the entry collection.
def add_data(D, R, P1, D1, S1, P2, D2, S2):
    return entry_repository.add_entry(R, P1, D1, S1, P2, D2, S2, D)
