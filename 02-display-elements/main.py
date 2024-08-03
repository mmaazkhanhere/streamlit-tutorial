import streamlit as st
import pandas as pd

# st.write can be used for all sorts of things like markdown, code, heading etc

st.title('Stocks Data')

# takes three arguments 1)label, 2)value, 3)delta (change in value)

col1, col2, col3 = st.columns(3) # divide the page into three columns
col1.metric(label='Current Value', value='$452.59', delta='-$23.00')
col2.metric(label='24 hour change', value='-$23.00', delta='-0.12%')
col3.metric(label='7 day change', value='+$45.63', delta='+2.5%')

table = pd.DataFrame(
    {"Time": ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00'],
     "Price": [453.12, 452.59, 452.59, 451.12, 451.12, 450.63, 450.63, 450.63],
     "Change": ['-0.12%', '-0.12%', '-0.12%', '-0.12%', '-0.12%', '-0.12%', '-0.12%', '-0.12%']}
)

st.table(table)
