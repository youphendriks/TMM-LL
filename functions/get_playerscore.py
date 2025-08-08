from objects.repositories.entry_repository import entry_repository
from objects.repositories.jank_repository import jank_repository

# Pull data concerning a player from the collection.
def get_playerscore(player):
    points_entry = 0
    points_jank = 0
    fnms_joined = []
    items = entry_repository.get_entries()
    # Calculate points from games, attendance and jank awards
    try:
        for item in items:

            print("item:")
            print(item)
            print(player)
            if item["player1"] == player:
                print(f"item: {item}")
                # Check if fnm date in list, else add it
                datetime = item["datetime"]
                date = datetime.split(" ")
                date = date[0]
                print(f"date: {date}")
                if date in fnms_joined:
                    print("Date already in the list")
                else:
                    print("added to fnms_joined")
                    fnms_joined.append(date)
                score = item["score1"]
                scoreOP = item["score2"]
                if score > scoreOP:
                    # Add score for won game
                    points_entry += 3
                if score == scoreOP:
                    # Add score for a draw
                    points_entry += 1
            if item["player2"] == player:
                print(f"item: {item}")
                # Check if fnm date in list, else add it
                datetime = item["datetime"]
                date = datetime.split(" ")
                date = date[0]
                print(f"date: {date} ")
                if date in fnms_joined:
                    print("Date already in the list")
                else:
                    print("added to fnms_joined")
                    fnms_joined.append(date)
                score = item["score2"]
                scoreOP = item["score1"]
                if score > scoreOP:
                    # Add score for won game
                    points_entry += 3
                if score == scoreOP:
                    # Add score for a draw
                    points_entry += 1
    except Exception as e:
        print(e)
        print("No data for this player")
    points_attendance = len(fnms_joined)
    print(f"points_attendance: {points_attendance}")
    # Get points awarded in jank awards
    jank = jank_repository.get_all_jank()
    for jankiness in jank:
        if jankiness["playername"] == player:
            points_jank += jankiness["points"]
    score = points_entry + points_jank + points_attendance
    return score
