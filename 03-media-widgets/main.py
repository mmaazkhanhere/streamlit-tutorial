import streamlit as st

st.write("#Media Widgets")
st.markdown("### Image File")
st.image("image.png", caption="This an image I added", width=500)
st.audio("audio.mp3")


def change():
    print(st.session_state.checker)


state = st.checkbox("Followed", key="checker", on_change=change)
# the state of the checkbox is displayed in the terminal

radio_bts = st.radio(
    "In which country do you live?", options=("USA", "Australia", "Pakistan")
)
print(radio_bts)


def btn_click():
    print("Button click")


btn = st.button("Subscribe", on_click=btn_click)

select = st.selectbox(
    "What is your favorite programming languages",
    options=("Python", "JavaScript", "C++"),
)

multi_select = st.multiselect(
    "What is your favorite colors", options=("Red", "Green", "Blue")
)

slider = st.slider("How much you like streamlit?", max_value=10)

slt_slider = st.select_slider(
    "How much you like streamlit", options=("Not much", "Okay", "Quite good")
)

name = st.text_input("Enter your name", max_chars=60)
if name is not None:
    st.text(f"Welcome to streamlit {name}")

text_area = st.text_area("Enter your programming experience", max_chars=200)
date = st.date_input("Enter date")
time = st.time_input("Enter time")
