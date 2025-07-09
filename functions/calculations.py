import numpy as np
import pandas as pd
import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import functions

uri = (
    "mongodb+srv://"
    + st.secrets.mongo.username
    + ":"
    + st.secrets.mongo.password
    + "@tmm-ll.6siai.mongodb.net/?retryWrites=true&w=majority&appName=TMM-LL"
)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))


# Run all the calculations after an FNM
def calculations():
    update_rankings()
    update_deckstats()
    update_playerstats()


def update_rankings():
    db = client.TMMDB
    data = functions.get_data()
    players = functions.get_players()
    rankings = {}
    for player in players:
        print("player:")
        print(player)
        # playerset = db.players.find({"playername": player})
        # index = playerset["_id"]
        # Calculate points per player

        playerscore = functions.get_playerscore(player)
        print("playerscore:")
        print(playerscore)
        # Calculate points from jankawards
        # Update rankings collection in DB
        query_filter = {"playername": player}
        update_operation = {"$set": {"score": playerscore}}

        db.rankings.update_one(query_filter, update_operation, upsert=True)

    return 0


def update_deckstats():
    # Get list of decks
    # For each deck
    # Get win%
    return 0


def update_playerstats():
    # Get list of players
    # For each player
    # Calculate win%
    # list played decks
    return 0
