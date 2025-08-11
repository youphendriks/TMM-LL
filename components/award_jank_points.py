import datetime
import streamlit as st
import functions

def main():
    # Obtain needed data through functions from functions.py
    players = functions.get_players()

    container1 = st.container(border=True)
    container1.header("Award jankpoints", divider="gray")

    player = container1.selectbox(
        "Player",
        options=players,
        index=None,
        key="P1",
        format_func=lambda p: f"{p['playername']}",
        placeholder="Select player",
        accept_new_options=False,
    )


    points = container1.selectbox(
        "Points won",
        options=[1, 2, 3],
        key="jankpoints",
        index=None,
        placeholder="Number of jankpoints won.",
        help="Select number of jankpoints won",
        accept_new_options=False,
    )

    fnmdate = container1.date_input("Date of FNM", datetime.date(2025, 6, 6))

    if container1.button("Add points"):
        fnmdatestr = str(fnmdate)
        result = functions.add_jankpoint(player["_id"], points, fnmdatestr)
        st.write("The points were added to the database!")

if __name__ == "__main__":
    main()