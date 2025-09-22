import pandas as pd
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import functions


def main():
    # Obtain needed data through functions from functions.py
    players = functions.get_players()
    decks = functions.get_decks()
    rankings = functions.get_rankings()
    days, hours, minutes = functions.get_timer()

    # Banner
    st.image("pictures/TMM_DM_hori_smaller.png")

    # Container 1
    st.header("Welcome", divider="gray")

    st.write("Welcome to the Team Midgame Mulligan website!")

    st.write("We create a little competition during our FNM's for shits & giggles.")

    st.subheader("Current season: Season 2")

    st.write("Starting at FNM 4th of July 2025 and ending at FNM 9th of January 2026!")

    st.subheader("Join us!")

    st.write(
        "Feel free to join our FNM hosted by [Magus Games](https://www.magusgames.nl/winkel/nl/7-tickets)!"
    )
    st.write("We play 4 rounds of legacy on friday evenings starting 19:30.")
    st.write("The current location is:")

    st.write("Merodestraat 31, 6171 XM in Stein.")
    # Container 2
    st.header("Rankings", divider="gray")
    df = pd.DataFrame(
        rankings,
        columns=(
            "_id",
            "playername",
            "overallpoints",
            "playpoints",
            "attendancepoints",
            "jankpoints",
        ),
    )
    # df = df.drop(column, inplace=True, axis=1)

    print("df:")
    print(df)
    df.drop(df[df["playername"] == "Jank1"].index, inplace=True)
    df.drop(df[df["playername"] == "Jank2"].index, inplace=True)
    df.drop(df[df["playername"] == "Jank3"].index, inplace=True)
    df.drop(df[df["playername"] == "Bye"].index, inplace=True)
    df = df.sort_values(by=["overallpoints"], ascending=False)
    df.index = pd.RangeIndex(start=1, stop=len(df.index) + 1, step=1)

    # Rename for display
    df_display = df.rename(
        columns={
            "playername": "Player Name",
            "overallpoints": "Overall Points",
            "playpoints": "Play Points",
            "attendancepoints": "Attendance Points",
            "jankpoints": "Jank Points",
        }
    )

    # Show in Streamlit
    st.dataframe(
        df_display,
        column_order=(
            "Player Name",
            "Overall Points",
            "Play Points",
            "Attendance Points",
            "Jank Points",
        ),
    )
    if st.button("Run calculations", use_container_width=True):
        result = functions.calculations()
        st.write("Calculations done!")

    # Container 3
    st.header("Jank awards", divider="gray")

    st.write("Voting closes on Sundays at 20:00!")
    st.write(
        "You have", days, "days,", hours, "hours and", minutes, "minutes left to vote!"
    )


if __name__ == "__main__":
    main()
