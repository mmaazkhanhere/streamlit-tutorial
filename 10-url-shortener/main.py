#pip install pyshorteners
#pip install pyperclip

import streamlit as st
import pyshorteners as pyst
import pyperclip

shortener = pyst.Shortener()

st.markdown("<h1 style='text-align:center;'>URL Shortener</h1>", unsafe_allow_html=True)


def copying():
    pyperclip.copy(shorted_url)
    

form = st.form("url")
url = form.text_input("Enter URL")
state = form.form_submit_button("SHORT")
if state:
    shorted_url = shortener.tinyurl.short(url)
    st.markdown("<h3>Shorted URL</h3>", unsafe_allow_html=True)
    st.markdown(f"<h6>{shorted_url}</h6>", unsafe_allow_html=True)
    st.button("Copy", on_click=copying)
    