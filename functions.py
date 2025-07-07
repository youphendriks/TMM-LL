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


# # Pull playernames from players collection.
def get_players():
    db = client.TMMDB
    items = db.players.find()
    players = []  # make hashable for st.cache_data
    for item in items:
        playername = str(item["firstname"] + " " + item["lastname"])
        players.append(playername)
    return players


# Pull decks from decks collection.
def get_decks():
    db = client.TMMDB
    items = db.decks.find()
    decks = []  # make hashable for st.cache_data
    for item in items:
        deckname = str(item["deckname"])
        decks.append(deckname)
    return decks


# Add score to the entry collection.
def add_score(P1, D1, S1, P2, D2, S2, date):
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


# Pull data from the collection.
def get_data():
    db = client.TMMDB
    items = db.TMM1.find()
    items = list(items)  # make hashable for st.cache_data
    return items


# Load player_rankings.
def get_rankings():
    db = client.TMMDB
    items = db.TMM1.find()
    items = list(items)  # make hashable for st.cache_data
    return items
