import streamlit as st

import functions
from objects.repositories.deck_repository import deck_repository


def main():

    decks = functions.get_decks()

    # Banner
    st.image("pictures/TMM_DM_hori_smaller.png")

    # Container 1
    st.header("Select a deck", divider="gray")

    D = st.selectbox(
        "Deck",
        options=decks,
        key="D",
        index=None,
        format_func=lambda d: f"{d['deckname']}",
        placeholder="Select a deck",
        accept_new_options=False,
    )
    if st.button("See stats", use_container_width=True):
        deckstats = list(deck_repository.get_deckstats(D))


if __name__ == "__main__":
    main()

