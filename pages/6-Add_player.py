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
def add_player(firstname, lastname):
    db = client.TMMDB
    items = db.players.insert_one({"firstname":firstname, "lastname":lastname})
    return items

container1 = st.container(border=True)
container1.header("Add player", divider="gray")
firstname = container1.text_input('First name')
lastname = container1.text_input('Last name')

if container1.button('Add player'):
    result = add_player(firstname, lastname)
    st.write('%s %s was added to players!' % (firstname, lastname) )
