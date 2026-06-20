from Bio import SeqIO
def find_motif_in_fasta(fasta_file, motif):
    sequences =SeqIO.parse(fasta_file, "fasta")
    sequences_with_motif = []
    for record in sequences:
        if motif in record.seq:
            sequences_with_motif.append(record)
    return sequences_with_motif