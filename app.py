import streamlit as st

from modules.dnatools import dna_tools
from modules.fastz import read_fasta

global sequence
tools = ["DNA Analysis", "FASTA Reader","Convert to FASTA"]
choice = st.sidebar.selectbox("Select a tool", tools)
if choice == "DNA Analysis":
    st.title("DNA Analysis Tool")
    sequence=st.text_input("Enter a DNA sequence:", "ATGCGTACGTTAGC")

    if st.button("Analyze"):
      results = dna_tools(sequence)
      st.write(f"Length: {results['length']}")
      st.write(f"Complement: {results['complement']}")
      st.write(f"Transcription: {results['transcription']}")
      st.write(f"Translation: {results['translation']}")
      st.write(f"GC Content: {results['gc_content']:.2f}%")
      st.write(f"Reverse Complement: {results['reverse_complement']}")

elif choice == "FASTA Reader":
    st.title("FASTA Reader Tool")
    fasta_file = st.file_uploader("Upload a FASTA file", type=["fasta","fa"])
    if(fasta_file.type is not "fasta" and fasta_file.type is not "fa"):
        st.error("Please upload a valid FASTA file or go to convert your file to FASTA format using the 'Convert to FASTA' tool.")

    if fasta_file is not None:
        results = read_fasta(fasta_file)
        st.write(f"ID: {results[0]}")
        st.write(f"Description: {results[1]}")
        st.write(f"Accession: {results[2]}")
        st.write(f"Sequence: {results[3]}")

elif choice == "Convert to FASTA":
    st.title("Convert to FASTA Tool")
    file = st.file_uploader("Upload a file to convert to FASTA", type=["gb","gbk","genbank","gbff","embl","emb"])

    if file is not None:
        file_con=file.format("fasta")
        st.download_button(
            label="Download FASTA file",
            data=file_con,
            file_name="converted.fasta",
            mime="text/plain"
        )

