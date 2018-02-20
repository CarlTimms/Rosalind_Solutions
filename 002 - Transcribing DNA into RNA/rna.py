#!/usr/bin/env python3

"""

    'rna.py'

        rosalind.info/problems/rna

    Carl Timms
    17.02.2018

"""


import sys


try:
    with open(sys.argv[1], 'r') as f_in, open(sys.argv[1] + '-output.txt', 'w') as f_out:
        data_set = f_in.read().rstrip()
        f_out.write(data_set.replace('T', 'U'))

except Exception as e:
    print("Failed with exception:", e)
