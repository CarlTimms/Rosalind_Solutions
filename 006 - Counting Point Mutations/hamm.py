#!/usr/bin/env python3

"""

    'hamm.py'

        rosalind.info/problems/hamm

    Carl Timms
    16.02.2018

"""


import sys

with open(sys.argv[1], 'r') as f_in, open(sys.argv[1].split('.')[0] + '-OUTPUT.txt', 'w') as f_out:
    data_set = f_in.read().rstrip()

    hamm_dist = 0

    m = (len(data_set) // 2) + 1 # Index of the first letter of the second string.
    for i in range(m - 1):
        if data_set[i] != data_set[i + m]:
            hamm_dist +=1

    f_out.write(str(hamm_dist))


