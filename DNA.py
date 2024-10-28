def counting_DNA_nucleotides(s):
    a_count = s.count('A') #counts the occurrence of A
    c_count = s.count('C') #counts the occurrence of C
    g_count = s.count('G') #counts the occurrence of G
    t_count = s.count('T') #counts the occurrence of T
    return f"{a_count} {c_count} {g_count} {t_count}"

#sample dataset
dna_string = '''GCCCTGGCCTACGCCTCGGGAGCAACTTGAACAGAGGAATCGTGAGAGCGACTATCCGAGCTCTCAGATGTCCGCAGCCAATTCGGAACTGAGTTGGGCTCTTTATAATGTCCC
AAGCTACGGGCCTTAAGTAAACCTCCTGCCTGGATAAGCGAATCTCATGAAGAGGTAAAAATGTTATCAGTCATCCGAAGCCGGTGAAACGCGGAGGCATTGAACTCTCATGGCTGGAGCTCCTGCTTTA
TACTACAGACCTTCTGTATCTGTTTTTGCGTCAGTCTACCATAGAACAGAGAATTCCATTCTTCTTATCACTCCTTCTTAGTTCAAGGATTCTGTAATCCCACAGAAGCGTTGCTATTTTCTACGACCAA
GGTATACCCGCTAATAAACTCGGACTCGCAGCCTATAGCCTCTTAGTCAAAAATCTGACCGAGTAGAATGACACCCCTCTAGTGCTATTCATAGCTCATGAGTACCCTACCCGCACTTTATACGTTAAAC
GCATAGTGCCCAAGACAGGGATACCGTGTTCACGAACGTTGAGTCGCCTTAAGGCAATGATACGAGTGAGAGGTAGCCTTAGACCATGAAGGAGGGGCCCCGAAAAAGGGAACTCTCAAGTCTAATTGCC
CGTATCGTTATATGCATGCATTAGCTTCTCCCGAACTATGGGATCAGTATCGTTCCCTCGAGAAGACACGGTTGGCTCTTTCTACAGGGTCAAAAGCACGAAACCGAGTAGAACCCGCAACTGCTGTGTC
CGCTAAACGACCGACGTGGGAATCGAGCGACCTCGTTAGCTTCATACTAAAGAACGCACTAGATCCCATGTTATAATCACGTTCGAGCGGGATCTACACGTTCCATTGCGAG'''
result = counting_DNA_nucleotides(dna_string)
print(result)