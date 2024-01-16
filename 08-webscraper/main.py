import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title='Web Scrapper')

st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)

with st.form("Search Form"):
    keyword: str = st.text_input("Enter keyword")
    state = st.form_submit_button("Search")

placeholder = st.empty()

if keyword:
    request_page = requests.get(f'https://unsplash.com/s/photos/{keyword}')
    st.write(request_page.status_code)
    soup = BeautifulSoup(request_page.content, 'lxml')
    rows = soup.find_all('div', class_='ripi6')
    
    col1, col2 = st.columns(2)
    for index, row in enumerate(rows):
        figures = row.find_all('figure')
        for i in range(2):
            img = figures[i].find('img', class_='zmDAx')
            list = img['srcset'].split("?")
            anchor = figures[i].find("a", class_='MorZF')
            if i == 0:
                col1.image(list[0])
                btn = col1.button("Download", key=str(index) + str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com/s"+anchor['href'])
            else:
                col2.image(list[0])
                btn = col2.button("Download", key=str(index) + str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor['href'])