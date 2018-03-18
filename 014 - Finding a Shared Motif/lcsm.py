#!/usr/bin/env python3

"""

    'lcsm.py'

        rosalind.info/problems/lcsm

    Carl Timms
    19.03.2018

"""


try:
    with open("rosalind_lcsm.txt", 'r') as f_in, open("rosalind_lcsm-OUTPUT.txt", 'w') as f_out:
        # Read from file in FASTA format
        fasta = f_in.read()

        # Create a list of the DNA strings
        dna_strings = [s[s.find('\n'):].replace('\n', '') for s in fasta.split('>')[1:]]

        # Find longest common substring
        longest_common_substring = ""
        start, end = 0, 1  # Start/end indices for substring slicing
        while end <= len(dna_strings[0]) - 1:
            # Identify the current substring
            sub = dna_strings[0][start: end]

            # Check if substring does not occur in any of the dna strings
            common_sub = True
            for s in dna_strings[1:]:
                if sub not in s:
                    common_sub = False
                    break

            # If substring exists in all DNA strings, record it and increment the end variable to search for a longer
            # substring in the next iteration
            if common_sub:
                longest_common_substring = sub
                end += 1

            # If substring does not exist in all DNA strings, search for a different substring of the same length in the
            # next iteration
            else:
                start += 1
                end += 1

        # Write the longest common substring to file and print
        f_out.write(longest_common_substring)
        print("Longest common substring:\n\t" + longest_common_substring)

except Exception as e:
    print("Failed with exception:", e)
