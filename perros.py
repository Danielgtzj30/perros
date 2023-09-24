import pickle
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth

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
if authenticator_status == True:
    st.warning("You have entered")

authenticator.logout("Logout", "sidebar")
st.sidebar.title(f"Welcome{name}")
