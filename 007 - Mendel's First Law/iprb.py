#!/usr/bin/env python3

"""

    'iprb.py'

        rosalind.info/problems/iprb

    Carl Timms & Katherine Murray
    20.02.2018

"""


import sys


with open(sys.argv[1], 'r') as f_in, open(sys.argv[1].split('.')[0] + '-OUTPUT.txt', 'w') as f_out:
    data = f_in.read().rstrip()

    k, m, n = [int(i) for i in data.split(' ')]
    total = k + m + n

    probability = ((k / total) * ((k - 1) / (total - 1))) + \
                  ((k / total) * (m / (total - 1))) + \
                  ((k / total) * (n / (total - 1))) + \
                  ((m / total) * (k / (total - 1))) + \
                  (((m / total) * ((m - 1) / (total - 1))) * 0.75) + \
                  (((m / total) * (n / (total - 1))) * 0.5) + \
                  (((n / total) * (m / (total - 1))) * 0.5) + \
                  ((n / total) * (k / (total - 1)))

    f_out.write(str(probability))
