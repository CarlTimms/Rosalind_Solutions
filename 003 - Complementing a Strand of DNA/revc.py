#!/usr/bin/env python3

"""

    'revc.py'

        rosalind.info/problems/revc

    Carl Timms
    17.02.2018

"""


import sys

try:
    with open(sys.argv[1], 'r') as f_in, open(sys.argv[1].split('.')[0] + '-OUTPUT.txt', 'w') as f_out:
        data_set = f_in.read().rstrip()
        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        reverse_complement = ''.join([comp[b] for b in data_set[::-1]])
        f_out.write(reverse_complement)

except Exception as e:
    print("Failed with exception:", e)







