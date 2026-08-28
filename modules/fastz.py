
from Bio import SeqIO
def read_fasta(fasta_file):
    sequences = list(SeqIO.parse(fasta_file, "fasta"))
    if fasta_file is not None:
     for seq in sequences:
        id=seq.id#using predefined functions to parse for and store respective information in variables
        description=seq.description
        accession=seq.annotations
        sequence=seq.seq

    return id, description, accession, sequence
