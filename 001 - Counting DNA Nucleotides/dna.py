#!/usr/bin/env python3

"""

    'dna.py'

        http://rosalind.info/problems/dna/

    Carl Timms
    16.02.2018

"""


import sys

try:
    with open(sys.argv[1], 'r') as f_in, open(sys.argv[1] + '-output', 'w') as f_out:
        dataset = f_in.read().rstrip()

        bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for base in dataset:
            bases[base] += 1

        f_out.write("{} {} {} {}".format(*[bases[b] for b in "ACGT"]))

except Exception as e:
    print("Failed with exception:", e)
