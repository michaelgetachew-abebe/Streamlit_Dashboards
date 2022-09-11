import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image

# Import the Logo image for NFL

image = Image.open('logo.jpg')
st.title("NFL DASHBOARD")
st.subheader("NFL Football Stats Explorer")
st.image(image, use_column_width=True)

st.markdown('''
This app performs simple webscraping of NFL Football stats 
''')

st.sidebar.header("User Input Features")

stat_type = ['Passing', 'Rushing', 'Receiving', 'Defense', 'Scoring']
st.sidebar.selectbox('Stat Type')
# Sidebar - Year selection
selected_year = st.sidebar.selectbox("Year", range(2000,2022))

# Function that performs the necessary Web Scraping of NFL player stats
# https://www.pro-football-reference.com/years/2019/rushing.htm
@st.cache
def data_loader(year, stat_type):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/" + str(stat_type) + ".htm"
    html = pd.read_html(url, header=1)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    player_stats = raw.drop(['Rk'], axis = 1)
    return player_stats

player_stats = data_loader(selected_year, stat)

#Sidebar - Team selection
sorted_unique_team = sorted(player_stats.Tm.unique())
selected_team = st.sidebar.multiselect('Team',sorted_unique_team, sorted_unique_team)

#Sidebar - Position Selection
sorted_unique_position = ['RB','QB','WR','FB','TE']
selected_pos = st.sidebar.multiselect('Position', sorted_unique_position, sorted_unique_position)

selected_data_frame = player_stats[(player_stats.Tm.isin(selected_team)) & (player_stats.Pos.isin(selected_pos))]

st.header('Player Satats of Selected Team(s)')
st.write('Data Dimension: ' + str(selected_data_frame.shape[0] + ' rows and ' + str(selecte_data_frame.shape[1]) + ' columns.'))
st.dataframe(selected_data_frame)

def filedownloader(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    herf = f'<a herf = "data:file/csv:base64,{b64}>" download = "playerstats.csv">Download CSV File</a>'
    return herf

st.markdown(filedownloader(selected_data_frame), unsafe_allow_html=True)

#Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    selected_data_frame.to_csv('output.csv', index=False)
    data_frame = pd.read_csv('output.csv')

    corr = data_frame.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask = mask, vmax=1, square=True)
    st.pyplot()