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
def add_jankpoint(playername, points, fnmdate):
    db = client.TMMDB
    items = db.jank.insert_one(
        {"playername": playername, "points": points, "fnm": fnmdate}
    )
    return items
