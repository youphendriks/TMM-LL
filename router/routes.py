def get_routes():
    return {
        "Home": {"component": "home", "roles": None},
        "Info": {"component": "info", "roles": None},
        "Player Stats": {"component": "playerstats", "roles": None},
        "Deck Stats": {"component": "deckstats", "roles": None},
        "Profile": {"component": "profile", "roles": ["user", "admin"]},
        "Input": {"component": "input", "roles": ["admin"]},
        "Add Player": {"component": "add_player", "roles": ["admin"]},
        "Add Deck": {"component": "add_deck", "roles": ["admin"]},
        "Award Jank Points": {"component": "award_jank_points", "roles": ["admin"]},
        "Calculations": {"component": "calculations", "roles": ["admin"]},
        "Jank Poll": {"component": "jank_poll", "roles": ["admin"]},
    }