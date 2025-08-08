from objects.repositories.jank_repository import jank_repository

# Add jank points for player to DB
def add_jankpoint(playername, points, fnmdate):
    return jank_repository.add_jank_points_for_player(playername, points, fnmdate)
