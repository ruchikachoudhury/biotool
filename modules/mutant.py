from Bio import pairwise2
from Bio.pairwise2 import format_alignment
def mutation_analysis(seq1,seq2):
    alignment = pairwise2.align.globalxx(seq1,seq2)
    #positions of mutations
    if len(seq1)==len(seq2):
        mutations = []
        for i in range(len(alignment[0][0])):
            if alignment[0][0][i] != alignment[0][1][i]:
                mutations.append(i)
    else:
        mutations = None

    return alignment, mutations
