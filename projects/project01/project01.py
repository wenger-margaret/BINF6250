#!/usr/bin/env python
from pprint import pprint


# Modify this function signature and fill in the details
def parse_line(line: str):

    pass


# Modify this function signature and fill in the details
def read_file(file: str):
    tally = {} # Dictionary initialization for counting diseases
    with open(file) as f: # open the file
        for line in f:
            if (line.startswith("#")): continue  # filters out metadata lines
                continue
            diseases = parse_line(line) # List of diseases

            for disease in diseases: # Counter loop for each disease in list
                if disease in tally:
                    tally[disease] += 1
                else:
                    tally[disease] = 1
    return tally         



if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
