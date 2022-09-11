import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from PIL import Image

# Add the logo image
image = Image('logo.jpg')
st.image(image, use_column_width=True)