import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as pd
import seaborn as sns
import numpy as np
from PIL import Image

# Import the Logo image for NFL

image = Image.open('logo.jpg')
st.title("NFL DASHBOARD")
st.subheader("NFL Football Stats (Rushing) Explorer")
st.image(image, use_column_width=True)