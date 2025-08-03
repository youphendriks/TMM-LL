# functions/layout.py
import streamlit as st

def header():
    with st.container():
        left, right = st.columns([0.6, 0.4], vertical_alignment= "center")
        with left:
            markdown_left, empty_right = st.columns([0.8, 0.2],)
            with markdown_left:
                if st.user.is_logged_in:
                    st.markdown(f":bust_in_silhouette: Logged in as: `{st.user.name}`")
        with right:
            empty_left, button_right = st.columns([0.5,0.5])
            with button_right:
                if not st.user.is_logged_in:
                    if st.button("Log in"):
                        st.login("google")
                else:
                    if st.button("Log out"):
                        st.logout()   
