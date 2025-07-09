import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = (
    "mongodb+srv://"
    + st.secrets.mongo.username
    + ":"
    + st.secrets.mongo.password
    + "@tmm-ll.6siai.mongodb.net/?retryWrites=true&w=majority&appName=TMM-LL"
)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))


# Add score to the entry collection.
def add_data(P1, D1, S1, P2, D2, S2, date):
    db = client.TMMDB
    items = db.entry.insert_one(
        {
            "player1": P1,
            "deck1": D1,
            "score1": S1,
            "player2": P2,
            "deck2": D2,
            "score2": S2,
            "date": date,
        }
    )
    return items
