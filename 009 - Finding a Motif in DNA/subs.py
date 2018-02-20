#!/usr/bin/env python3

"""

    'subs.py'

        rosalind.info/problems/subs

    Carl Timms
    21.02.2018

"""


import sys

with open(sys.argv[1], 'r') as f_in, open(sys.argv[1].split('.')[0] + '-OUTPUT.txt', 'w') as f_out:
    data = f_in.read().rstrip()

    dna_string, motif = data.split('\n')

    locations = []
    match = dna_string.find(motif, 0)
    while match != -1:
        locations.append(str(match + 1))
        match = dna_string.find(motif, match + 2)

    f_out.write(' '.join(locations))
