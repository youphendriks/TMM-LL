import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client

# Add score to the entry collection.
def add_data(R, P1, D1, S1, P2, D2, S2, datetime):
    db = db_client.get_client().TMMDB
    items = db.entry.insert_one(
        {
            "round": R,
            "player1": P1,
            "deck1": D1,
            "score1": S1,
            "player2": P2,
            "deck2": D2,
            "score2": S2,
            "datetime": datetime,
        }
    )
    return items
