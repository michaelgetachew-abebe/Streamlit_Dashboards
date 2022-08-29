# Import the packages to be used in this script

import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# Page title and header contents

image = Image.open('logo.jpg')

st.title("BIOINFORMATICS DASHBOARD")
st.image(image, use_column_width = True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition od query DNA!!!
""")

# Input textbox

# This box queries the user to enter the DNA sequence
st.header("Enter DNA sequence?")

input_sequence = ">>DNA QUERY\nGAACACGTGGAG ..."

sequence = st.text_area("Sequence input", input_sequence, height = 300)
