import streamlit as st
from objects.repositories.user_repository import user_repository

@st.cache_data
def get_user_profile():
    return user_repository.get_user_by_idp_id(st.user["sub"])