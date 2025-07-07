import numpy as np
import pandas as pd
import pymongo
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import functions

# Obtain needed data through functions from functions.py
players = functions.get_players()
decks = functions.get_decks()

# Banner
st.image("pictures/TMM_DM_hori_smaller.png")

# Container 1
st.header("Welcome", divider="gray")

st.write("Some text about Team Midgame Mulligan.")

# Container 2
st.header("Rankings", divider="gray")
df = pd.DataFrame(np.random.randn(50, 2), columns=("Player name", "Points"))
df.index = pd.RangeIndex(start=1, stop=51, step=1)
st.dataframe(df)

# Container 3
st.header("Jank awards", divider="gray")
