#!/usr/bin/env python3

"""

    'fib.py'

        rosalind.info/problems/fib

    Carl Timms
    18.02.2018

"""


import sys

try:
    with open(sys.argv[1], 'r') as f_in:
        parameters = f_in.read().rstrip().split(' ')

        n = int(parameters[0])  # Number of months
        k = int(parameters[1])  # Pairs per litter

        gen_a, gen_b = 1, 1
        for i in range(2, n):
            gen_n = gen_b + (gen_a * k)  # The current generation size. From recurrence relation Fn = Fn-1 + (Fn-2) * k
            gen_a, gen_b = gen_b, gen_n

        print("Rabbits after {} months (k = {} pairs per litter) =".format(n, k), gen_b)

except Exception as e:
    print("Failed with exception:", e)
