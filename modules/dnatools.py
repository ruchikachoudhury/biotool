import streamlit as st
from Bio.Seq import Seq
sequence=st.text_input("Enter a DNA sequence:", "ATGCGTACGTTAGC")
if st.button("Analyze"):
    st.write("Length of the sequence:", len(sequence))