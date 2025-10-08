import streamlit as st

import functions
from objects.database_client import db_client
from objects.repositories.entry_repository import entry_repository


# Run all the calculations after an FNM
def calculations():
    update_rankings()
    update_deckstats()
    # update_playerstats()


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
    total_matches = entry_repository.get_total_matches()
    total_games = entry_repository.get_total_games()

    print(f"total_matches: {total_matches}")
    print(f"total_games: {total_games}")
    # For each deck
    for deck in decks:
        # Get matches played, match win %, games played and game win %
        deck_stats = functions.calculate_deck_stats(deck)
        # Update rankings collection in DB
        query_filter = {"deck": deck_stats["deck"]}
        update_operation = {
            "$set": {
                "match_count": deck_stats["match_count"],
                "match_win_percentage": deck_stats["match_win_percentage"],
                "games_count": deck_stats["games_count"],
                "game_win_percentage": deck_stats["game_win_percentage"],
            }
        }
        print(f"Update operation : {update_operation}")
        db.deck_stats.update_one(query_filter, update_operation, upsert=True)

        # get stats vs other decks
        # vs_deck_stats = functions.calculate_vs_deck_stats(deck, entries)
        # Get player with highest win% and most games with the deck [TODO]

        # Update data in DB
    return 0


def update_playerstats():
    # Get list of players
    # For each player
    # Calculate win%
    # list played decks
    return 0
