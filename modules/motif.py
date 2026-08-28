from Bio import SeqIO
def find_motif_in_fasta(fasta_file, motif):#bringing arguments such as the fasta file and the motif or the sepcific region you wanna look for
    sequences =SeqIO.parse(fasta_file, "fasta")#parsing through the fasta file
    sequences_with_motif = []#initializing 
    for record in sequences:#using loop to look through the fasta with the specific motif given
        if motif in record.seq:
            sequences_with_motif.append(record)#stores if found
    return sequences_with_motif
