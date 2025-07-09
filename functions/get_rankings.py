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


# Load player_rankings.
def get_rankings():
    db = client.TMMDB
    items = db.rankings.find()
    items = list(items)  # make hashable for st.cache_data
    print("items get_rankings:")
    print(items)
    return items
