import pandas as pd
import streamlit as st

import functions
from objects.repositories.deck_repository import deck_repository


def main():

    deckstats = functions.get_deckstats()
    decks = functions.get_decks()

    # Banner
    st.image("pictures/TMM_DM_hori_smaller.png")

    df = pd.DataFrame(
        deckstats,
        columns=(
            "_id",
            "deck",
            "game_win_percentage",
            "games_count",
            "match_count",
            "match_win_percentage",
            "games_win",
            "match_win",
        ),
    )

    df.drop(df[df["deck"] == "Unknown"].index, inplace=True)
    df.drop(df[df["deck"] == "Bye bitches"].index, inplace=True)
    df = df.sort_values(by=["match_win_percentage"], ascending=False)
    print("df:")
    print(df)
    # Do for each deck in deckstats
    for (
        _id,
        deck,
        game_win_percentage,
        games_count,
        match_count,
        match_win_percentage,
        games_win,
        match_win,
    ) in df.items():
        print("match_count:")
        print(match_count)
        if match_count < 8:
            continue
        else:
            GWperc = "{:.0%}".format(game_win_percentage)
            MWperc = "{:.0%}".format(match_win_percentage)
            D = deck
            MWP = str(MWperc)
            st.divider()

            # Break into 2 columns
            col1, col2 = st.columns([6, 6], gap="large")
            # Deckname
            col1.subheader("Deck: " + D)
            col2.subheader("Round win: " + MWP)

            # Round win %
            MWT = col1.text("Round win %:")
            MWP = col2.text(MWperc)

            # Game win %
            GWT = col1.text("Game win %:")
            GWP = col2.text(GWperc)

            # Rounds played
            RP = col1.text("Rounds played:")
            RW = col2.text(deck["match_count"])

            # Games played
            GR = col1.text("Games played:")
            GW = col2.text(deck["games_count"])


if __name__ == "__main__":
    main()
