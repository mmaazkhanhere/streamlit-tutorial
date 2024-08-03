import streamlit as st

st.title("Welcome to Streamlit Tutorial")
st.header('Media Widgets')
st.image('image.png', caption='This is a certification image', width=500)

st.audio("audio.mp3")


# def change():
#     print(st.session_state.checker)

st.write('Page followed?')
st.checkbox("Followed")

radio_bts = st.radio(
    'Select the country you live in.', options = ("USA", "Australia", "Pakistan", "India")
)

btn = st.button("Subscribe")


select = st.selectbox(
    "What is your favorite programming languages",
    options=("Python", "JavaScript", "C++"),
)

multi_select = st.multiselect(
    "In which languages do you have proficiency?", options=("Python", "JavaScript", "Typescript", "GO", "Ruby", "Rust"), default=("Typescript")
)

slider = st.slider("How much do you like streamlit", max_value=10)

slt_slider = st.select_slider("How much you like streamlit", options=('Not much', 'Okay', 'Very much'))


name = st.text_input("Enter your name", max_chars=40)
if len(name) > 0:
    st.text(f"Welcome to streamlit {name}")

# text_area = st.text_area("Enter your programming experience", max_chars=200)

text_area = st.text_area("Enter your programming experience", placeholder="I started my programming when ...")

date = st.date_input("Enter date")
time = st.time_input("Enter time")
