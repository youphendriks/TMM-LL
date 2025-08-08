import numpy as np
import pandas as pd
import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import functions
from functions.get_layout import header

header()

container1 = st.container(border=True)
container1.header("Add deck", divider="gray")
deckname = container1.text_input("Deck name")

if container1.button("Add Deck"):
    result = functions.add_deck(deckname)
    st.write("%s was added to decks!" % (result["deckname"]))
