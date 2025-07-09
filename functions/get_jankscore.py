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


# Get current jank of the week points information
def get_jankscore():
    db = client.TMMDB
    items = db.players.find()
    players = []  # make hashable for st.cache_data
    for item in items:
        playername = str(item["firstname"] + " " + item["lastname"])
        players.append(playername)
    return players
