import streamlit as st
from Bio.Seq import Seq

sequence=st.text_input("Enter a DNA sequence:", "ATGCGTACGTTAGC")

if st.button("Analyze"):
    # Create a Seq object
    dna_seq = Seq(sequence)
    
    # Calculate GC content
    gc_content = (dna_seq.count("G") + dna_seq.count("C")) / len(dna_seq) * 100
    
    # Get the reverse complement
    reverse_complement = dna_seq.reverse_complement()
    
    # Display results
    st.write(f"GC Content: {gc_content:.2f}%")
    st.write(f"Reverse Complement: {reverse_complement}")