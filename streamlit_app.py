import streamlit as st
import pandas as pd

# pg = st.navigation([st.Page("pages/1-home.py"), st.Page("pages/2-stats.py"), st.Page("pages/3-info.py"), st.Page("pages/4-add-deck.py"), st.Page("pages/5-fix-error.py")])

x = st.slider("Select a value")
st.write(x, "squared is", x * x)
