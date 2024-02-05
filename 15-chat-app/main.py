import streamlit as st

prompt = st.chat_input("Say something")

if 'data' not in st.session_state:
    st.session_state.data = []

if prompt:
    st.session_state.data.append(prompt)
    st.write(f"User has sent the following prompt: {prompt}")

st.write(st.session_state.data)

