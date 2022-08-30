#Import the necessary packages for the dashboard

import streamlit as st
import pandas as pd
import base64
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as sns

# Header sections of the dashboard
image = Image.open('bryant-logo.webp')

st.title("NBA DASHBOARD")
st.subheader("NBA PLAYER STATS EXPLORER")
st.image(image, use_column_width = True)

st.markdown("""
This app performs simple webscrapping of NBA player stat dataset
* **Data Source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

#Web scraping of player stats
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) #Deletes repeating headers in the response content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis = 1)
    return playerstats

# Add slider and adjust the dashboard to read for side bar selection
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2021))))
playerstats = load_data(selected_year)

#Team selcetion
team_list = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team',team_list, team_list)