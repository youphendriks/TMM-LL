import streamlit as st
from datetime import datetime
from objects.repositories.player_repository import player_repository
from objects.repositories.user_repository import user_repository

def create_user_profile():
    # See if a player exists with the name of logged in user to link the profile to
    player = player_repository.get_player_by_name(st.user["given_name"], st.user["family_name"])
    player_id = player["_id"] if player else None
    # generate a profile according to the data passed by the IdP
    user_profile = {
        "playerid": player_id,
        "idpid": st.user["sub"],
        "email": st.user["email"],
        "emailverified": st.user["email_verified"],
        "name": st.user["name"],
        "givenname": st.user["given_name"],
        "familyname": st.user["family_name"],
        "roles": ["user"],
        "lastlogin": datetime.now()
    }

    new_user_id = user_repository.add_user(user_profile)
    return user_repository.get_user(new_user_id)