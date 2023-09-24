import pickle
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth
from io import StringIO
import pdfplumber
text = ''
#--- User Authentitactor -------
names = ["Daniel", "Jonny"]
usernames = ["JDaniel", "Djon"]


file_path = Path(__file__).parent/"hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords=pickle.load(file)

authenticator=stauth.Authenticate(names, usernames, hashed_passwords, "Hack2023", "abc", cookie_expiry_days=10)

name, authenticator_status, username = authenticator.login("Login", "main")

if authenticator_status == False:
    st.warning("Username/password is incorrect")
if authenticator_status == None:
    st.warning("Please enter your username and password")
#-----------------------InputFile----------------------------------

if authenticator_status == True:
    with st.sidebar:
        authenticator.logout("Logout", "sidebar")
        st.title("Libretas")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            #text = ''
            for page in pdf.pages:
             text += page.extract_text()
    learn="Hola"
    preguntaf="Cuantos años tienes?"
    respuestaf="Nose"
    if st.button("Learn"):
        st.write(learn)
    if st.button("Flashcards"):
        st.write(preguntaf)
        if st.button("Give Answer"):
            st.write(respuestaf)
    st.button("Quiz")
    



