#!/usr/bin/env python3

"""

    'grph.py'

        rosalind.info/problems/grph

    Carl Timms
    17.03.2018

"""


try:
    with open("rosalind_grph.txt", 'r') as f_in, open("rosalind_grph-OUTPUT.txt", 'w') as f_out:
        # Read data
        fasta = f_in.read().replace('\n', '')

        # Associates a DNA string with its ID string
        nodes = {}  # {'CTA...CTA': 'Rosalind_8833', ...}

        # Fill nodes{}
        for data in fasta.split('>')[1:]:
            nodes[data[13:]] = data[:13]

        # Output the adjacency list to file
        for dna in nodes:
            # Find the matching DNA strings
            matches = [n for n in nodes if dna[-3:] == n[:3] and dna != n]

            # Write a line to file for each match
            for match in matches:
                print("{} {}".format(nodes[dna], nodes[match]), file=f_out)

except Exception as e:
    print("Failed with exception:", e)













