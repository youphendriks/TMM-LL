import streamlit as st

import functions

container1 = st.container(border=True)
container1.header("Add player", divider="gray")
playername = container1.text_input("Insert your playername")

if container1.button("Add player"):
    result = functions.add_player(playername)
    st.write("%s was added to players!" % (playername))
