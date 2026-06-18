import streamlit as st
from Bio.Seq import Seq
st.write("DNA Sequence Analysis Tool")
sequence=st.text_input("Enter a DNA sequence:", "ATGCGTACGTTAGC")
if st.button("Analyze"):
    st.write("Length of the sequence:", len(sequence))
    st.write("complement of the sequence:", Seq(sequence).complement())
    st.write("transcription of the sequence:", Seq(sequence).transcribe())
    st.write("translation of the sequence:", Seq(sequence).translate())
