import streamlit as st
import numpy as np
import pandas as pd
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

container1 = st.container(border=True)
container1.header("Input", divider="gray")

uri ="mongodb+srv://"+st.secrets.mongo.username+":"+st.secrets.mongo.password+"@tmm-ll.6siai.mongodb.net/?retryWrites=true&w=majority&appName=TMM-LL"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Pull playernames from players collection.
@st.cache_data(ttl=600)
def get_players():
    db = client.TMMDB
    items = db.players.find()
    players = []# make hashable for st.cache_data
    for item in items:
        playername = str(item["firstname"] +" "+ item["lastname"])
        players.append(playername)
    return players 

players = get_players()

# Pull decks from decks collection.
@st.cache_data(ttl=600)
def get_decks():
    db = client.TMMDB
    items = db.decks.find()
    decks = []# make hashable for st.cache_data
    for item in items:
        deckname = str(item["deckname"]) 
        decks.append(deckname)
    return decks 

decks = get_decks()

# Add score to the entry collection.
@st.cache_data(ttl=600)
def add_score(P1, D1, S1, P2, D2, S2):
    db = client.TMMDB
    items = db.entry.insert_one({"player1": P1, "deck1": D1, "score1": S1,
                                 "player2": P2, "deck2":D2, "score2": S2})
    return items

col1, col2 = container1.columns([3, 3], gap = "large")

col1.subheader("Player 1")

P1 = col1.selectbox(
    "Player 1",
    options= players,
    index=None,
    key= "P1",
    placeholder="Select player 1",
    help="If your name is not in the list, add it on the 'Add player' page!",
    accept_new_options=False,
)

D1 = col1.selectbox(
    "Deck player 1",
    options= decks,
    index=None,
    key= "D1",
    placeholder="Select player 1's deck",
    help="If your deck is not in the list, add it on the 'Add deck' page!",
    accept_new_options=False,
)

S1 = col1.selectbox(
    "Game wins player 1",
    options= [0,1,2],
    index=None,
    key= "S1",
    placeholder="Player 1 game wins.",
    help="Select number of game wins",
    accept_new_options=False,
)


col2.subheader("Player 2")

P2 = col2.selectbox(
    "Player 2",
    options= players,
    key= "P2",
    index=None,
    placeholder="Select player 2",
    help="If your name is not in the list, add it on the 'Add player' page!",
    accept_new_options=False,
)

D2 = col2.selectbox(
    "Deck player 2",
    options= decks,
    key= "D2",
    index=None,
    placeholder="Select player 2's deck",
    help="If your deck is not in the list, add it on the 'Add deck' page!",
    accept_new_options=False,
)

S2 = col2.selectbox(
    "Game wins player 2",
    options= [0,1,2],
    key= "S2",
    index=None,
    placeholder="Player 2 game wins.",
    help="Select number of game wins",
    accept_new_options=False,
)


if container1.button('Submit score', use_container_width=True):
    if 'P1' not in st.session_state:
        container1.write("Please check and make sure everything is filled in.")
    else:
        result = add_score(P1, D1, S1, P2, D2, S2)
        container1.write('Your score was added!')


container2 = st.container(border=True)
container2.header("Rankings", divider="gray")
df = pd.DataFrame(np.random.randn(50, 3), columns=("col %d" % i for i in range(3)))
container2.dataframe(df)

container3 = st.container(border=True)
container3.header("Jank awards", divider="gray")
