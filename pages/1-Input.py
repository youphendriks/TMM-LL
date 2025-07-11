from datetime import date, datetime, timedelta

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
st.header("Input", divider="gray")

col1, col2 = st.columns([3, 3], gap="large")

col1.subheader("Player 1")

R = col1.selectbox(
    "Round",
    options=[1, 2, 3, 4],
    index=None,
    key="R",
    placeholder="Select the round",
    accept_new_options=False,
)


P1 = col1.selectbox(
    "Player 1",
    options=players,
    index=None,
    key="P1",
    placeholder="Select player 1",
    help="If your name is not in the list, add it on the 'Add player' page!",
    accept_new_options=False,
)

D1 = col1.selectbox(
    "Deck player 1",
    options=decks,
    index=None,
    key="D1",
    placeholder="Select player 1's deck",
    help="If your deck is not in the list, add it on the 'Add deck' page!",
    accept_new_options=False,
)

S1 = col1.selectbox(
    "Game wins player 1",
    options=[0, 1, 2],
    index=None,
    key="S1",
    placeholder="Player 1 game wins.",
    help="Select number of game wins",
    accept_new_options=False,
)

col2.subheader("Player 2")

P2 = col2.selectbox(
    "Player 2",
    options=players,
    key="P2",
    index=None,
    placeholder="Select player 2",
    help="If your name is not in the list, add it on the 'Add player' page!",
    accept_new_options=False,
)

D2 = col2.selectbox(
    "Deck player 2",
    options=decks,
    key="D2",
    index=None,
    placeholder="Select player 2's deck",
    help="If your deck is not in the list, add it on the 'Add deck' page!",
    accept_new_options=False,
)

S2 = col2.selectbox(
    "Game wins player 2",
    options=[0, 1, 2],
    key="S2",
    index=None,
    placeholder="Player 2 game wins.",
    help="Select number of game wins",
    accept_new_options=False,
)

if st.button("Submit score", use_container_width=True):
    datetime = datetime.today()
    result = functions.add_data(R, P1, D1, S1, P2, D2, S2, str(datetime))
    st.write("Your score was added!")
