import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client

# Add deck to DB
def add_deck(deckname):
    db = db_client.get_client().TMMDB
    items = db.decks.insert_one({"deckname": deckname})
    return items
