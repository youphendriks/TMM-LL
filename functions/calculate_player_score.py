from datetime import datetime

from objects.repositories.entry_repository import entry_repository
from objects.repositories.jank_repository import jank_repository


def calculate_player_score(player):
    print(f"Calculating score for: {player}")
    # retrieve entries for calculation
    player_id = player["_id"]
    playername = player["playername"]
    # put in list to make non consumable
    entries = list(entry_repository.get_entries_for_player(playername))
    print("Entries:")
    for entry in entries:
        print(entry)
    play_points = calculate_play_points(entries, player_id)
    attendance_points = calculate_attendance(entries)
    jank_points = calculate_jank_points(player_id)
    # sum up all totals for overall points gained
    overall_points = play_points + attendance_points + jank_points
    # return object with distinct point distribution
    return {
        "playername": playername,
        "overall_points": overall_points,
        "play_points": play_points,
        "attendance_points": attendance_points,
        "jank_points": jank_points,
    }


def calculate_play_points(entries, player_id):
    play_points_total = 0

    for entry in entries:
        player_score, opp_score = determine_match_scores(entry, player_id)
        print(f"player_score: {player_score}")
        print(f"opp_score: {opp_score}")
        play_points_total += calculate_match_points(
            player_score, opp_score
        )
        print(f"play_points_total: {play_points_total}")

    return play_points_total


def determine_match_scores(entry, player_id):
    player_score = 0
    opp_score = 0
    if entry["player1"] == player_id:
        player_score = entry["score1"]
        opp_score = entry["score2"]
    else:
        player_score = entry["score2"]
        opp_score = entry["score1"]

    return {"player_score": player_score, "opp_score": opp_score}


def calculate_match_points(player_score, opp_score):
    if player_score > opp_score:
        return 3

    if player_score == opp_score:
        return 1

    return 0


def calculate_attendance(entries):
    unique_dates = {
        (
            entry["datetime"].date()
            if isinstance(entry["datetime"], datetime)
            else datetime.fromisoformat(entry["datetime"]).date()
        )
        for entry in entries
    }
    return len(unique_dates)


def calculate_jank_points(player_id):
    jank_entries = jank_repository.get_jank_for_player(player_id)

    total_jank = 0
    for jank in jank_entries:
        total_jank += jank["points"]

    return total_jank
