import numpy as np
import pandas as pd
import streamlit as st

import functions

# View entries last 7 days

# View jank awards score
st.write("Please don't use this :P")

if st.button("Run calculations", use_container_width=True):
    result = functions.calculations()
    st.write("Calculations done!")
