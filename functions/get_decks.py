import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client

# Pull decks from decks collection.
def get_decks():
    db = db_client.get_client().TMMDB
    items = db.decks.find()
    decks = []  # make hashable for st.cache_data
    for item in items:
        deckname = str(item["deckname"])
        decks.append(deckname)
    return decks
