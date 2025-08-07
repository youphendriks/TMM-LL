import numpy as np
import pandas as pd
import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client
import functions

# Run all the calculations after an FNM
def calculations():
    update_rankings()
    update_deckstats()
    update_playerstats()


def update_rankings():
    db = db_client.get_client().TMMDB
    players = functions.get_players()
    for player in players:
        print("player:")
        print(player)
        # Calculate points per player
        playerscore = functions.get_playerscore(player)
        print(f"playerscore:{playerscore}")
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
