import streamlit as st

import functions

container1 = st.container(border=True)
container1.header("Add player", divider="gray")
st.write(
    "You can use any name you want, your full name is fine, your first name and a nickname (example: Loamlad Youp) or maybe just a nickname."
)
playername = container1.text_input("Insert your playername")

if container1.button("Add player"):
    result = functions.add_player(playername)
    st.write("%s was added to players!" % (playername))
