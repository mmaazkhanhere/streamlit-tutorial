import streamlit as st

st.title('Counter')

if 'count' not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)

increment = col1.button('Increment') 
decrement = col3.button('Decrement')

if increment:
    st.session_state.count += 1

if decrement:
    st.session_state.count -= 1

col2.subheader(f"Count: {st.session_state.count}")