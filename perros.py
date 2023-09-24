import pickle
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth
from io import StringIO
import pdfplumber
from PIL import Image
import time

def typing_animation(text):
    for char in text:
        st.text(char)
        time.sleep(0.1)  # Adjust the sleep duration for typing speed
text = ''
#--- User Authentitactor -------
col2, col4 = st.columns([1,3])
with col4:
    st.title('Study...By Yourself ✏️')
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
#col2, col4 = st.columns([1,0.1])
#with col4:
if authenticator_status == True:
    with st.sidebar:
        st.subheader("New Note..................+")
        st.divider()
        st.title("Libretas 📓")
        st.button("Control")
        st.button("Power Units")
        st.button("Quick Prototyping")
        st.button("Mexican History")
        st.button("Project Managment")
        st.button("German")
        st.button("Circuits 101")
        st.button("Circuits Lab")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            #text = ''
            for page in pdf.pages:
             text += page.extract_text()
    learn="Hola"
    preguntaf="Cuantos años tienes?"
    respuestaf="Nose"
    respuestaqu="Nose"

    if st.checkbox("Learn📖"):
        st.write(learn)
    if st.checkbox("Flashcards📇"):
        st.write(preguntaf)
        Respuesta = st.button('Show answer!')
        if Respuesta:
            st.write(respuestaf)

    if st.checkbox("Quiz📝"):
        st.write(preguntaf)
        res = st.text_input('Type yours answer')
    col2, col4 = st.columns([1,0.15])
    with col4:
        authenticator.logout("Logout")

    



