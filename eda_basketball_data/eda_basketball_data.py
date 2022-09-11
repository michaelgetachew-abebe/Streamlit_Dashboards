#Import the necessary packages for the dashboard

import streamlit as st
import pandas as pd
import base64
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
@st.cache # Improves the user engagement in the model
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

#Player position selection
position_list = ['C','PF','SF','PG','SG']
selected_position = st.sidebar.multiselect('Position', position_list, position_list)

#Data Filtering
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_position))]
st.header('Display PLayer Stats of Selectd Team(s)')
st.write('Data Dimensions: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]))
st.dataframe(df_selected_team)

def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()