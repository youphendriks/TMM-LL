import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client

# Get current jank of the week points information
def get_jankscore():
    db = db_client.get_client().TMMDB
    items = db.players.find()
    players = []  # make hashable for st.cache_data
    for item in items:
        playername = str(item["firstname"] + " " + item["lastname"])
        players.append(playername)
    return players
