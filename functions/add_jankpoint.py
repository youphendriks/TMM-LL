import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client

# Add player to DB
def add_jankpoint(playername, points, fnmdate):
    db = db_client.get_client().TMMDB
    items = db.jank.insert_one(
        {"playername": playername, "points": points, "fnm": fnmdate}
    )
    return items
