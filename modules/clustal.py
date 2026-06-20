from Bio import AlignIO
def read_alignment(msa_file,t):
    alignment = AlignIO.read(msa_file, "fasta")
    summaryalign=AlignIO.SummaryInfo(alignment)
     #Searching for conserved sequences in the alignment
    conserved_sites = []
    for i in range(alignment.get_alignment_length()):
        column = alignment[:, i]
        if len(set(column)) == 1:
            conserved_sites.append(i)
    #Searching for variable sequences in the alignment
    variable_sites = []
    for i in range(alignment.get_alignment_length()):
        column = alignment[:, i]
        if len(set(column)) > 1:
            variable_sites.append(i)
    #Searching for consensus sequences in the alignment
    consensus = summaryalign.dumb_consensus(Threshold=t, ambiguous='N')
    return conserved_sites, variable_sites, consensus