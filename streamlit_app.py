import numpy as np
import pandas as pd
import streamlit as st

chart_data = pd.DataFrame(
    np.random.randn(1000, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

