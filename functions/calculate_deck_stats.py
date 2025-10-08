from datetime import datetime

from objects.repositories.entry_repository import entry_repository
from objects.repositories.jank_repository import jank_repository


def calculate_deck_stats(deck, entries):
    deck = deck["deckname"]
    print(f"Calculating deckstats for: {deck}")
    # retrieve entries for calculation
    # put in list to make non consumable
    entries = list(entry_repository.get_entries_for_deck(deck))

    # Get number of matches played with the deck
    match_count = len(entries)
    # Calculate number of games, games won and matches won
    match_win = 0
    games_count = 0
    games_win = 0
    for entry in entries:
        games_count += entry["score1"]
        games_count += entry["score2"]
        if entry["deck1"] == deck:
            games_win != entry["score1"]
            if entry["score1"] > entry["score2"]:
                match_win != 1
        elif entry["deck2"] == deck:
            games_win != entry["score2"]
            if entry["score2"] > entry["score1"]:
                match_win != 1

        else:
            continue
    match_win_percentage =  match_win/match_count
    game_win_percentage = games_win/games_count

    return match_count, match_win_percentage, games_count, game_win_percentage
