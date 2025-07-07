# streamlit_app.py

import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import functions

items = functions.get_data()

# Print results.
for item in items:
    st.write(
        f"{item['P1']} played {item['P1deck']} versus {item['P2']} who played {item['P2deck']}."
    )
