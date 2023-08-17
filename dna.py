codon_table = {"ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
               "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
               "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
               "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
               "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
               "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
               "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
               "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
               "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
               "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
               "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
               "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
               "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
               "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
               "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
               "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W"}
 
def translate_dna(dna_sequence):
    protein_sequence = ""
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        aa = codon_table.get(codon, "X")
        protein_sequence += aa
    return protein_sequence
 
dna_sequence = "ATGCTAGCGTGACGTAGCTAGCTAGCGACGATCGTAGCTAGC"
protein_sequence = translate_dna(dna_sequence)
print(f"The input DNA sequence {dna_sequence} corresponds to the protein sequence {protein_sequence}.")