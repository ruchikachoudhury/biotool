import streamlit as st
from Bio import SeqIO

st.write("FASTA Reader")
fasta_file = st.file_uploader("Upload a FASTA file", type="fasta")
if fasta_file is not None:
    sequences = list(SeqIO.parse(fasta_file, "fasta"))
    for seq in sequences:
        st.write(f"ID: {seq.id}")
        st.write(f"Description: {seq.description}")
        st.write(f"Sequence: {seq.seq}")

