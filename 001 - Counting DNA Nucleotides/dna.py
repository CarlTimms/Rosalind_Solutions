#!/usr/bin/env python3

"""

    'dna.py'

        rosalind.info/problems/dna

    Carl Timms
    16.02.2018

"""


import sys

try:
    with open(sys.argv[1], 'r') as f_in, open(sys.argv[1].split('.')[0] + '-OUTPUT.txt', 'w') as f_out:
        data_set = f_in.read().rstrip()

        bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for base in data_set:
            bases[base] += 1

        f_out.write("{} {} {} {}".format(*[bases[b] for b in "ACGT"]))

except Exception as e:
    print("Failed with exception:", e)
