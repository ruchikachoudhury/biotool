from Bio import AlignIO
def read_alignment(msa_file,t):
    alignment = AlignIO.read(msa_file, "fasta")#reading the multiple sequence alignment file, making sure the file uploaded is in fasta format
    summaryalign=AlignIO.SummaryInfo(alignment)#summary of the alignment
     #Searching for conserved sequences in the alignment
    conserved_sites = []#initializing array
    for i in range(alignment.get_alignment_length()):#using the loop till the entire length of aligned section
        column = alignment[:, i]#going through each row and storing all the values in that column as a string
        if len(set(column)) == 1:#if string is only 1, only one amino acid exists
            conserved_sites.append(i)#storing the conserved sites
    #Searching for variable sequences in the alignment
    variable_sites = []
    for i in range(alignment.get_alignment_length()):
        column = alignment[:, i]
        if len(set(column)) > 1:#more than 1 means variability exists, using set() because it counts redundant values as 1
            variable_sites.append(i)#storing all the variable sites
    #Searching for consensus sequences in the alignment
    consensus = summaryalign.dumb_consensus(Threshold=t, ambiguous='N')
    return conserved_sites, variable_sites, consensus#returning values 
