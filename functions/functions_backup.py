from datetime import datetime, time, timedelta

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


# Add player to DB
def add_player(firstname, lastname):
    db = client.TMMDB
    items = db.players.insert_one({"firstname": firstname, "lastname": lastname})
    return items


# Add deck to DB
def add_deck(deckname):
    db = client.TMMDB
    items = db.decks.insert_one({"deckname": deckname})
    return items


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


# Get time untill sunday 20:00
def get_timer():
    today = datetime.today()
    t = datetime.combine(today.date() + timedelta((6 - today.weekday()) % 7), time(20))
    if today > t:
        t += timedelta(7)
    delta = t - today
    totalSeconds = delta.total_seconds()
    days, left = divmod(totalSeconds, 86400)
    hours, remainder = divmod(left, 3600)
    minutes, seconds = divmod(remainder, 60)

    return int(days), int(hours), int(minutes)
