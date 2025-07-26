# main.py

import analyzer

def main():
    seq = input("Enter a DNA sequence (A, T, G, C only): ").strip().upper()

    if not analyzer.validate_dna(seq):
        print("❌ Invalid DNA sequence. Only A, T, G, C are allowed.")
        return

    print("\n✅ DNA Sequence is Valid")
    print("Nucleotide Frequency:", analyzer.nucleotide_frequency(seq))
    print("GC Content:", analyzer.gc_content(seq), "%")
    print("Transcribed RNA:", analyzer.transcribe_dna(seq))
    print("Reverse Complement:", analyzer.reverse_complement(seq))

if __name__ == "__main__":
    main()
