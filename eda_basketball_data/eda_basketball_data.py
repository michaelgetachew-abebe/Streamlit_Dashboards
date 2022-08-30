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