import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from objects.database_client import db_client

# Pull data from the collection.
def get_data():
    db = db_client.get_client().TMMDB
    items = db.TMM1.find()
    items = list(items)  # make hashable for st.cache_data
    return items
