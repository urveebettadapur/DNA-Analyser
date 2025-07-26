# analyzer.py

def validate_dna(seq):
    valid_nucleotides = {'A', 'T', 'G', 'C'}
    return all(nuc in valid_nucleotides for nuc in seq.upper())

def nucleotide_frequency(seq):
    freq = {}
    for nucleotide in seq.upper():
        freq[nucleotide] = freq.get(nucleotide, 0) + 1
    return freq

def gc_content(seq):
    seq = seq.upper()
    gc_count = seq.count('G') + seq.count('C')
    return round((gc_count / len(seq)) * 100, 2)

def transcribe_dna(seq):
    return seq.upper().replace('T', 'U')

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[nuc] for nuc in reversed(seq.upper()))
