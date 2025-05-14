import streamlit as st
import numpy as np
import pandas as pd

container1 = st.container(border=True)
container1.header("Scoring", divider="gray")

container2 = st.container(border=True)
container2.header("Stats explained", divider="gray")
df = pd.DataFrame(np.random.randn(50, 3), columns=("col %d" % i for i in range(3)))
container2.dataframe(df)

