from objects.repositories.jank_repository import jank_repository

# Add jank points for player to DB
def add_jankpoint(player_id, points, fnmdate):
    return jank_repository.add_jank_points_for_player(player_id, points, fnmdate)
