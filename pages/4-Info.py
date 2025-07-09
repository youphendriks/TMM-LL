import numpy as np
import pandas as pd
import streamlit as st

container1 = st.container(border=True)
container1.header("Scoring", divider="gray")
container1.write("Scoring is simple;")
container1.write("Winning a round earns you 3 points.")
container1.write("Draws earn you 1 point.")
container1.write("A loss earns you 0 points.")

container2 = st.container(border=True)
container2.header("Jank awards info", divider="gray")
container2.write("Information about the jank awards;")
container2.write("Every week you can earn points by playing jank decks!")
container2.subheader("What's at stake?")
container2.write(
    "Every FNM you can enter your jank deck into the comperition. Everyone can vote on the deck they think is the best jank. On sunday evenings at 20:00 voting will stop and the winners will be declared!"
)
container2.write("The following points will be awarded to the winners;")
container2.write("1st place: 7 points")
container2.write("2nd place: 5 points")
container2.write("3rd place: 3 points")

container2.subheader("How to join")
container2.write(
    "Joining is simple; just send me (Youp) a link to your jank brew (preferably moxfield) BEFORE thursday 20:00 and I'll add you to the competition! You can make last minute changes to your deck so no stress! Just let me know if you decide to not play the brew at all!"
)
container2.write(
    "What qualifies as a jank brew? Well that's hard to say! I hope people will vote on innovative ideas, so I'll be lenient about entries."
)

container3 = st.container(border=True)
container3.header("Stats explained", divider="gray")
container3.write(
    "This is where I would place my explanation about the stats...IF I HAD ANY!."
)
