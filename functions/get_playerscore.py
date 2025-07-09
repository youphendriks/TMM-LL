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


# Pull data concerning a player from the collection.
def get_playerscore(player):
    points_entry = 0
    points_jank = 0
    db = client.TMMDB
    items = db.entry.find()
    for item in items:
        print("item:")
        print(item)
        if item["player1"] == player:
            score = item["score1"]
            scoreOP = item["score2"]
            if score > scoreOP:
                points_entry += 3
            if score == scoreOP:
                points_entry += 1
        if item["player2"] == player:
            score = item["score2"]
            scoreOP = item["score1"]
            if score > scoreOP:
                points_entry += 3
            if score == scoreOP:
                points_entry += 1
    score = points_entry + points_jank
    return score
