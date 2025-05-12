# streamlit_app.py

import streamlit as st
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri ="mongodb+srv://"+st.secrets.mongo.username+":"+st.secrets.mongo.password+"@tmm-ll.6siai.mongodb.net/?retryWrites=true&w=majority&appName=TMM-LL"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.TMMDB
    items = db.TMM1.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['P1']} played {item['P1deck']} versus {item['P2']} who played {item['P2deck']}.")
