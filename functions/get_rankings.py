import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from objects.database_client import db_client


# Load player_rankings.
def get_rankings():
    db = db_client.get_client().TMMDB
    items = db.rankings.find()
    items = list(items)  # make hashable for st.cache_data
    print("items get_rankings:")
    print(items)
    return items
