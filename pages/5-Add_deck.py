import streamlit as st
import numpy as np
import pandas as pd
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri ="mongodb+srv://"+st.secrets.mongo.username+":"+st.secrets.mongo.password+"@tmm-ll.6siai.mongodb.net/?retryWrites=true&w=majority&appName=TMM-LL"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def add_player(deckname):
    db = client.TMMDB
    items = db.decks.insert_one({"deckname":deckname})
    return items

container1 = st.container(border=True)
container1.header("Add deck", divider="gray")
deckname= container1.text_input('Deck name')

if container1.button('Add Deck'):
    result = add_player(deckname)
    st.write('%s was added to decks!' % (deckname) )
