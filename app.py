import streamlit as st





from modules.motif import find_motif_in_fasta

global sequence
tools = ["DNA Analysis", "FASTA Reader","Convert to FASTA","Entrez Gene Info","MSA Viewer","mutation analysis", "PDB Parser","Motif Finder"]
choice = st.sidebar.selectbox("Select a tool", tools)
if choice == "DNA Analysis":
    from modules.dnatools import dna_tools
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

elif choice == "PDB Parser":
    from modules.pdb import parse_pdb_file
    st.title("PDB Parser Tool")
    pdb_file = st.file_uploader("Upload a PDB file", type=["pdb"])

    if pdb_file is not None:
        structure = parse_pdb_file(pdb_file)

elif choice == "FASTA Reader":
    from modules.fastz import read_fasta
    st.title("FASTA Reader Tool")
    fasta_file = st.file_uploader("Upload a FASTA file", type=["fasta","fa"])

    if fasta_file is not None:
        filename = getattr(fasta_file, "name", "")
        if not filename.lower().endswith((".fasta", ".fa")):
            st.error("Please upload a valid FASTA file (extension .fasta or .fa) or go to convert your file to FASTA format using the 'Convert to FASTA' tool.")
        else:
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


elif choice == "Entrez Gene Info":
    from modules.eEntrez import fetch_gene_info
    st.title("Entrez Gene Info Tool")
    gene_id = st.text_input("Enter a gene ID:", "12345")
    email = st.text_input("Enter your email:", "user@example.com")
    dbtype = st.selectbox("Select database type:", ["gene", "nucleotide", "protein"])
    if st.button("Fetch Info"):
        results = fetch_gene_info(gene_id, email, dbtype)
        if results:
            st.write(f"Gene Name: {results['gene_name']}")
            st.write(f"Gene Description: {results['gene_description']}")
            st.write(f"Gene Organism: {results['gene_organism']}")
        else:
            st.error("No information found for the given gene ID.")

elif choice == "MSA Viewer":
    from modules.clustal import read_alignment
    st.title("Multiple Sequence Alignment (MSA) Viewer Tool")
    msa_file = st.file_uploader("Upload a MSA file", type=["fasta","fa","clustal","aln"])
    t = st.text_input("Consensus Threshold", "0.7")
    if msa_file is not None:
        filename = getattr(msa_file, "name", "")
        if not filename.lower().endswith((".fasta", ".fa", ".clustal", ".aln")):
            st.error("Please upload a valid MSA file (extension .fasta, .fa, .clustal, or .aln).")
        else:
            def read_alignment(msa_file,t):
                return read_alignment(msa_file,t)
            results = read_alignment(msa_file,t)
            st.write(f"Conserved Sites: {results[0]}")
            st.write(f"Variable Sites: {results[1]}")
            st.write(f"Consensus Sequence: {results[2]}")

elif choice == "mutation analysis":
    from modules.mutant import mutation_analysis
    st.title("Mutation Analysis Tool")
    seq1 = st.text_input("Enter the first DNA sequence:", "ATGCGTACGTTAGC")
    seq2 = st.text_input("Enter the second DNA sequence:", "ATGCGTACGTTAGC")
    if st.button("Analyze Mutations"):
        from modules.mutant import mutation_analysis
        alignment, mutations = mutation_analysis(seq1, seq2)
        results = mutation_analysis(seq1, seq2)
        st.write("Alignment:" + str(alignment))
        if mutations is not None:
            st.write(f"Positions of mutations: {mutations}")
        else:
            st.write("The sequences are of different lengths; mutation positions cannot be determined.")

elif choice == "Motif Finder":
    from modules.motif import find_motif_in_fasta
    st.title("Motif Finder Tool")
    fasta_file = st.file_uploader("Upload a FASTA file", type=["fasta","fa"])
    motif = st.text_input("Enter a motif to search for:", "ATG")
    if fasta_file is not None and motif:
        filename = getattr(fasta_file, "name", "")
        if not filename.lower().endswith((".fasta", ".fa")):
            st.error("Please upload a valid FASTA file (extension .fasta or .fa) or go to convert your file to FASTA format using the 'Convert to FASTA' tool.")
        else:
            results = find_motif_in_fasta(fasta_file, motif)
            if results:
                st.write(f"Sequences containing the motif '{motif}':")
                for record in results:
                    st.write(f"ID: {record.id}, Description: {record.description}")
            else:
                st.write(f"No sequences found containing the motif '{motif}'.")