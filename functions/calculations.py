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
        # Calculate points per player
        playerscore = functions.get_playerscore(player)
        # Calculate points from jankawards
        # Update rankings collection in DB
        db.rankings.update_one(
            {"playername": player["playername"], "score": playerscore}, upsert=True
        )

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
