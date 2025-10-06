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
    deck_match_count = len(entries)
    # Calculate number of games
    deck_games_count = 0
    for entry in entries:
        deck_games_count += entry["score1"]
        deck_games_count += entry["score2"]

