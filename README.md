Live Demo
https://biotools.streamlit.app/

Overview
Biotools or Bioinormatics Toolkit is a web application made using streamlit, python and bioython. It is a collection of various bioinformatic tools for the analysis of various types of biological data. The tools include DNA analysis, FASTA reader, Entrez gene info, MSA viewer, mutation analysis, PDB parser and motif finder. The application is designed to be user-friendly and easy to use for both beginners and experts in the field of bioinformatics.
This application was build to explore computational biology and bioinformatics and get hands on experience on bioinformatics software development. The application is designed to be user-friendly and easy to use for both beginners and experts in the field of bioinformatics.

Features
- DNA Analysis: This tool allows users to analyze DNA sequences by calculating the GC content, reverse complement, and other properties of the sequence.
- FASTA Reader: This tool allows users to read and visualize FASTA files, which are commonly used to store biological sequences.
- Convert to FASTA: This tool allows users to convert other file formats to FASTA format
- Entrez Gene Info: This tool allows users to retrieve information about genes from the NCBI Entrez database.
- MSA Viewer: This tool allows users to view multiple sequence alignments (MSA)
- Mutation Analysis: This tool allows users to analyze mutations in DNA sequences by comparing two sequences and identifying the differences between them.
- PDB Parser: This tool allows users to parse and visualize Protein Data Bank (PDB) files, which contain 3D structures of proteins and other biological macromolecules.
- Motif Finder: This tool allows users to find motifs in FASTA files, which are short, recurring patterns in biological sequences that are often associated with specific functions or structures.

Technologies Used
- Streamlit
- Python
- Biopython
- Git
- GitHub

Project Structure
The project is structured as follows:
|-- app.py: The main application file
|-- requirements.txt: the file containing the required packages for the application
|-- modules/: A directory containing the various modules for the different tools in the application
    |-- dnatools.py
    |-- fastz.py
    |-- eEntrez.py
    |-- clustal.py
    |-- mutant.py
    |-- pdb.py
    |-- motif.py
|-- README.md: This file

Installation
Clone the repository by using the following command:
``` git clone https://github.com/ruchikachoudhury/biotool.git ```
Navigate to the project directory:
``` cd biotool ```
Install the required packages:
``` pip install -r requirements.txt ```
Run the application:
``` streamlit run app.py ```

Author
Ruchika Choudhury
B.Sc. Biotechnology 
Interested in Bioinformatics and Computational Biology
