from datetime import datetime

import streamlit as st

import functions


def main():
    # Obtain needed data through functions from functions.py
    players = functions.get_players()
    decks = functions.get_decks()
    today = datetime.today().strftime("%Y-%m-%d")
    # Banner
    st.image("pictures/TMM_DM_hori_smaller.png")

    # Container 1
    st.header("Input", divider="gray")

    D = st.date_input("Date of FNM", today)

    R = st.selectbox(
        "Round",
        options=[1, 2, 3, 4],
        index=None,
        key="R",
        placeholder="Select the round",
        accept_new_options=False,
    )

    col1, col2 = st.columns([3, 3], gap="large")

    col1.subheader("Player 1")

    P1 = col1.selectbox(
        "Player 1",
        options=players,
        index=None,
        key="P1",
        format_func=lambda p: f"{p['playername']}",
        placeholder="Select player 1",
        help="If your name is not in the list, add it on the 'Add player' page!",
        accept_new_options=False,
    )

    D1 = col1.selectbox(
        "Deck player 1",
        options=decks,
        index=None,
        key="D1",
        format_func=lambda d: f"{d['deckname']}",
        placeholder="Select player 1's deck",
        help="If your deck is not in the list, add it on the 'Add deck' page!",
        accept_new_options=False,
    )

    S1 = col1.selectbox(
        "Game wins player 1",
        options=[0, 1, 2],
        index=None,
        key="S1",
        placeholder="Player 1 game wins.",
        help="Select number of game wins",
        accept_new_options=False,
    )

    col2.subheader("Player 2")

    P2 = col2.selectbox(
        "Player 2",
        options=players,
        key="P2",
        format_func=lambda p: f"{p['playername']}",
        index=None,
        placeholder="Select player 2",
        help="If your name is not in the list, add it on the 'Add player' page!",
        accept_new_options=False,
    )

    D2 = col2.selectbox(
        "Deck player 2",
        options=decks,
        key="D2",
        index=None,
        format_func=lambda d: f"{d['deckname']}",
        placeholder="Select player 2's deck",
        help="If your deck is not in the list, add it on the 'Add deck' page!",
        accept_new_options=False,
    )

    S2 = col2.selectbox(
        "Game wins player 2",
        options=[0, 1, 2],
        key="S2",
        index=None,
        placeholder="Player 2 game wins.",
        help="Select number of game wins",
        accept_new_options=False,
    )

    if st.button("Submit score", use_container_width=True):
        print("Input is:")
        print(f"R:{R}")
        print(f"P1:{P1}")
        print(f"D1:{D1}")
        print(f"S1:{S1}")
        print(f"P2:{P2}")
        print(f"D2:{D2}")
        print(f"S2:{S2}")
        print(f"D:{D}")

        result = functions.add_data(R, P1, D1, S1, P2, D2, S2, D)
        st.write("Your score was added!")


if __name__ == "__main__":
    main()
