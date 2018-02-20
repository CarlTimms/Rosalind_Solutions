#!/usr/bin/env python3

"""

    'prot.py'

        rosalind.info/problems/prot
    Carl Timms
    16.02.2018

"""


import sys

codon = {
    "GCU": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A',
    "UGU": 'C', "UGC": 'C',
    "GAU": 'D', "GAC": 'D',
    "GAA": 'E', "GAG": 'E',
    "UUU": 'F', "UUC": 'F',
    "GGU": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G',
    "CAU": 'H', "CAC": 'H',
    "AUU": 'I', "AUC": 'I', "AUA": 'I',
    "AAA": 'K', "AAG": 'K',
    "CUU": 'L', "CUC": 'L',  "CUA": 'L', "CUG": 'L',
    "UUA": 'L', "UUG": 'L',
    "AUG": 'M',
    "AAU": 'N', "AAC": 'N',
    "CCU": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
    "CAA": 'Q', "CAG": 'Q',
    "CGU": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R', "AGA": 'R', "AGG": 'R',
    "UCU": 'S', "UCC": 'S', "UCA": 'S', "UCG": 'S', "AGU": 'S', "AGC": 'S',
    "ACU": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T',
    "GUU": 'V', "GUC": 'V', "GUA": 'V', "GUG": 'V',
    "UGG": 'W',
    "UAU": 'Y', "UAC": 'Y',
    "UAA":  '', "UAG":  '', "UGA": ''
    }

with open(sys.argv[1], 'r') as f_in, open(sys.argv[1].split('.')[0]  + '-output.txt', 'w') as f_out:
    data = f_in.read().rstrip()
    protein_string = ''.join([codon[data[i:i + 3]] for i in range(0, len(data), 3)])
    f_out.write(protein_string)
