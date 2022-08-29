# Import the packages to be used in this script

from asyncore import write
from itertools import count
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

input_sequence = ">>DNA QUERY\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGGTGCTCGGG\nTCGGGCAAACAGGAAGGTGAAGAAGTATCCTATCAGGACGGAAGGTACGTCCTGGTGCGGAACAACT\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGGTGCTCGGG"

input_sequence = st.text_area("Sequence input", input_sequence, height = 300)
input_sequence = input_sequence.splitlines()
input_sequence = input_sequence[1:] # Remove the first line of the sequence ">>DNA QUERY" since it isn't part of the sequence!!!
input_sequence = ''.join(input_sequence) # Concatenate our the list sequence into a single string

st.header("INPUT")
input_sequence

st.header("OUTPUT")
st.subheader("1. Print Dictionary")

def DNA_nucleotide_count(seq):
  i = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return i

nucleotide_count = DNA_nucleotide_count(input_sequence)

st.write(nucleotide_count)

# Print a textual result of the nucleotide count

st.subheader("2, Print text")
A_count = f"There are {nucleotide_count['A']} adenine(A)"
T_count = f"There are {nucleotide_count['T']} thymine(T)"
G_count = f"There are {nucleotide_count['G']} guanine(G)"
C_count = f"There are {nucleotide_count['C']} cytosine(C)"
st.write(A_count)
st.write(T_count)
st.write(G_count)
st.write(C_count)

# Display the dataframe

