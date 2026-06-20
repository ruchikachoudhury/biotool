
from Bio.Seq import Seq

def dna_tools(sequence):
    sequence1 = Seq(sequence)
    length = len(sequence1)
    complement = sequence1.complement()
    transcription = sequence1.transcribe()
    translation = sequence1.translate()
    gc_content = (sequence1.count("G") + sequence1.count("C")) / length * 100
    reverse_complement = sequence1.reverse_complement()

    return {
        "length": str(length) + " amino acids",
        "complement": str(complement),
        "transcription (mRNA)": str(transcription),
        "translation (Protein)": str(translation),
        "gc_content": gc_content,
        "reverse_complement": str(reverse_complement),

    }

