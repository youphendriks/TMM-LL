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
def add_player(playername):
    db = client.TMMDB
    items = db.players.insert_one({"playername": playername})
    rankingentry = db.rankings.insert_one({"playername": playername, "score": 0})
    return items
