import streamlit as sl
import requests
from bs4 import BeautifulSoup
#sl.image("https://images.unsplash.com/photo-1599940824399-b87987ceb72a")
sl.markdown("<h1 style='text-align: center:'>Web Scrapper </h1>",unsafe_allow_html=True)
with sl.form("Search"):
    keyword=sl.text_input("Enter Your Key Word")
    search=sl.form_submit_button("Search")
    if search:
        page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup=BeautifulSoup(page.content, 'lxml')
        rows=soup.find_all("div", class_="ripi6")
        print(len(rows))
        #print(page.status_code)