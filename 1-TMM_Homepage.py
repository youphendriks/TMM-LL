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
rankings = functions.get_rankings()
days, hours, minutes = functions.get_timer()

# Banner
st.image("pictures/TMM_DM_hori_smaller.png")

# Container 1
st.header("Welcome", divider="gray")

st.write("Welcome to the Team Midgame Mulligan website!")

st.write("We create a little competition during our FNM's for shits & giggles.")

st.subheader("Current season: Season 2")

st.write("Starting at FNM 12th of July 2025 and ending at FNM 9th of January 2026!")

st.subheader("Join us!")

st.write(
    "Feel free to join our FNM hosted by [Magus Games](https://www.magusgames.nl/winkel/nl/7-tickets)!"
)
st.write("We play 4 rounds of legacy on friday evenings starting 19:30.")
st.write("The current location is:")

st.write("Merodestraat 31, 6171 XM in Stein.")
# Container 2
st.header("Rankings", divider="gray")
df = pd.DataFrame(rankings, columns=("_id", "playername", "score"))
# df = df.drop(column, inplace=True, axis=1)

print("df:")
print(df)
df = df.sort_values(by=["score"], ascending=False)
df.index = pd.RangeIndex(start=1, stop=len(df.index) + 1, step=1)
st.dataframe(df, column_order=("playername", "score"))

# Container 3
st.header("Jank awards", divider="gray")

st.write("Voting closes on Sundays at 20:00!")
st.write(
    "You have", days, "days,", hours, "hours and", minutes, "minutes left to vote!"
)
