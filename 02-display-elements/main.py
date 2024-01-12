import streamlit as st
import pandas as pd

# st.write can be used for all sorts of things like markdown, code, heading etc

st.write("## Heading 2")  # markdown style done with write

# takes three arguments 1)label, 2)value, 3)delta (change in value)
st.metric(label="Wind speed", value="1200 m/s", delta="-1.4 m/s")

table = pd.DataFrame(
    {"Column 1": [1, 2, 3, 4, 5, 6, 7], "Column 2": [11, 12, 13, 14, 15, 16, 17]}
)

st.table(table)
st.dataframe(table)
