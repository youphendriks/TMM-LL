import streamlit as st
import functions
from datetime import datetime

def main():
    # Ensure option_amount is an integer
    if "option_amount" in st.session_state:
        try:
            st.session_state["option_amount"] = int(st.session_state["option_amount"])
        except (ValueError, TypeError):
            st.session_state["option_amount"] = 1  # fallback default

    # data
    players = get_players()

    # layout
    st.subheader("Jank Poll")
    amount_of_options = st.number_input(
        'Amount of options',
        min_value=1,
        step=1,
        value=st.session_state.get("option_amount", 1),
        key="option_amount",
        format="%d"
    )
    
    st.button("Create poll", on_click=lambda: [create_poll(amount_of_options), reset_inputs()])

    grid = st.columns(2)

    for r in range(amount_of_options):
        add_option(grid, r, players)

# functions
def add_option(grid, option_number, players):
    with grid[0]:
        st.text_input("Deck name", key=f"option{option_number}")
    with grid[1]:
        st.selectbox(
            "Player",
            options=players,
            index=None,
            key=f"player{option_number}",
            format_func=lambda p: f"{p['playername']}",
            placeholder="Select player",
            accept_new_options=False,
        )

def create_poll(amount_of_options):
    functions.add_poll(format_poll_data(amount_of_options))

def format_poll_data(amount_of_options):
    options = []
    for i in range(amount_of_options):
        player = st.session_state.get(f"player{i}")
        print(player)
        if player is not None:
            options.append({
                "playername": st.session_state.get(f"player{i}")["playername"],
                "deck": st.session_state.get(f"option{i}")
            })
    
    return { "options": options, "date":  str(datetime.now().replace(second=0, microsecond=0)), "status": "open" }

def reset_inputs(min_options=1):
    for key in list(st.session_state.keys()):
        # Reset poll options
        if key.startswith("option"):
            st.session_state[key] = ""       # clear text input
        # Reset player selections
        elif key.startswith("player"):
            st.session_state[key] = None     # clear selectbox
        elif key == "option_amount":
            st.session_state[key] = int(min_options)

def get_players():
    return functions.get_players()


if __name__ == "__main__":
    main()