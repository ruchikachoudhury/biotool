import streamlit as st
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

st.write("Sequence Records")
sequence=st.text_input("Enter a DNA sequence:", "ATGCGTACGTTAGC")
id=st.text_input("Enter an ID for the sequence:", "Gene1")
description=st.text_input("Enter a description for the sequence:", "Example DNA sequence")
if st.button("Create Record"):
# Creating record using SeqRecord
    record=SeqRecord(Seq(sequence), id=id, description=description)