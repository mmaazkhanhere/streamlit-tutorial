import streamlit as st

st.title('Counter Example using Callbacks')

if 'count' not in st.session_state:
    st.session_state.count = 0

    
def increment_counter():
    st.session_state.count += 1

    
def decrement_counter():
    st.session_state.count -= 1


st.write('Count= ', st.session_state.count)
    
st.button('Increment Counter', on_click=increment_counter)
st.button('Decrement Counter', on_click=decrement_counter)

