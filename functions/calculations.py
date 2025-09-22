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
    db = db_client.get_client().TMMDB
    decks = functions.get_decks()

    # For each deck
    for deck in decks:

        # Get win%
        entries, round_count, win_percentage = (
            functions.calculate_deck_roundwin_percentage(deck)
        )
        print(
            "Deck: {} - Rounds player: {} - Win%:{}".format(
                deck, round_count, win_percentage
            )
        )
        # Get win% vs each other deck
        win_percentage_vs_decks = functions.calculate_deck_roundwin_vs_deck(
            deck, entries
        )
        # Get player with highest win% with the deck [TODO]

        # Update data in DB
    return 0


def update_playerstats():
    # Get list of players
    # For each player
    # Calculate win%
    # list played decks
    return 0
