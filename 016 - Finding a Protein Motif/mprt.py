#!/usr/bin/env python3

"""

    'mprt.py'

        rosalind.info/problems/mprt

    Carl Timms
    19.03.2018

"""


import re
import urllib.request

try:
    with open("rosalind_mprt.txt", 'r') as f_in, open("rosalind_mprt-OUTPUT.txt", 'w') as f_out:
        # Clear output file and read input file
        f_out.truncate()
        data = f_in.read()

        # List access IDs
        access_IDs = data.rstrip().split('\n')

        for a_id in access_IDs:
            try:
                # Request FASTA data from UniProt database
                fasta = urllib.request.urlopen("http://www.uniprot.org/uniprot/{}.fasta".format(a_id)).read().decode().rstrip()

                # Extract the DNA string from FASTA response
                dna_string = fasta[fasta.find('\n'):].replace('\n', '')

                # Find locations of N-glycosylation motif in the DNA string
                locations = [str(motif.start() + 1) for motif in re.finditer("(?=N[^P](S|T)[^P])", dna_string)]

                # If the N-glycosylation motif occurs in the DNA string, write to file
                if locations:
                    f_out.writelines(a_id + '\n' + ' '.join(locations) + '\n')

            except urllib.request.HTTPError as e:
                print("Exception on access ID \"{}\": \n\t{}".format(a_id, e))

except Exception as e:
    print("Failed with exception:", e)
