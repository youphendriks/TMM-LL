import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client

# Add player to DB
def add_player(playername):
    db = db_client.get_client().TMMDB
    items = db.players.insert_one({"playername": playername})
    rankingentry = db.rankings.insert_one({"playername": playername, "score": 0})
    return items
