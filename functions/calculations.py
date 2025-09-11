import streamlit as st

import functions
from objects.database_client import db_client


# Run all the calculations after an FNM
def calculations():
    update_rankings()
    update_deckstats()
    update_playerstats()


def update_rankings():
    db = db_client.get_client().TMMDB
    players = functions.get_players()
    print(f"Players:  {players}")
    for player in players:
        # Calculate points per player
        playerscore = functions.calculate_player_score(player)
        print(f"playerscore:{playerscore}")
        st.write(player["playername"])
        st.write(playerscore)
        # Update rankings collection in DB
        query_filter = {"playerid": player["_id"]}
        update_operation = {
            "$set": {
                "playername": playerscore["playername"],
                "overallpoints": playerscore["overall_points"],
                "playpoints": playerscore["play_points"],
                "attendancepoints": playerscore["attendance_points"],
                "jankpoints": playerscore["jank_points"],
            }
        }
        print(f"Update operation : {update_operation}")
        db.rankings.update_one(query_filter, update_operation, upsert=True)


def update_deckstats():
    # Get list of decks
    # For each deck
    # Get win%
    return 0


def update_playerstats():
    # Get list of players
    # For each player
    # Calculate win%
    # list played decks
    return 0
