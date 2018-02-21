#!/usr/bin/env python3

"""

    'cons.py'

        rosalind.info/problems/cons

    Carl Timms
    21.02.2018

"""


import sys

try:
    with open(sys.argv[1], 'r') as f_in, open(sys.argv[1].split('.')[0] + '-OUTPUT.txt', 'w') as f_out:
        data = f_in.read().split('>')[1:]
        dna_strings = [data[i][13:].replace('\n', '') for i in range(len(data))]

        counts, consensus_string, string_len = {}, "", len(dna_strings[0])
        for i in range(string_len):
            counts[i] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}  # Subdictionary created for each index.
            for seq in dna_strings:
                counts[i][seq[i]] +=1  # Increment the count of bases found at each index.
            consensus_string += max(counts[i], key=counts[i].get)  # Build the consensus string.

        # Write the consensus string and profile.
        print(consensus_string, file=f_out)
        for b in "ACGT":
            print("{}: {}".format(b, ' '.join([str(counts[i][b]) for i in range(string_len)])), file=f_out)

except Exception as e:
    print("Failed with exception:", e)
