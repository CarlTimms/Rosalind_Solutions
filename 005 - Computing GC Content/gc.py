#!/usr/bin/env python3

"""

    'gc.py'

        rosalind.info/problems/gc

    Carl Timms
    18.02.2018

"""


import sys

try:
    with open(sys.argv[1], 'r') as f_in, open(sys.argv[1] + '-output.txt', 'w') as f_out:
        fasta = f_in.read().replace('\n', '')

        max_id, max_gcc = "", 0

        for sequence in fasta.split('>')[1:]:
            dna_string = sequence[13:]
            gcc = (dna_string.count('G') + dna_string.count('C')) / len(dna_string)
            if gcc > max_gcc:
                max_id = sequence[:13]
                max_gcc = gcc

        f_out.write("{}\n{:6f}". format(max_id, max_gcc * 100))

except Exception as e:
    print("Failed with exception:", e)
