#!/usr/bin/env python
from pprint import pprint



def parse_line(line: str):
    
    info = line.split("\t")[7]

    # Create a dictionary to hold the key-value pairs from the INFO field
    info_dict = {}
    for pair in info.split(";"):
        key, value = pair.split("=")
        info_dict[key] = value
    
    # Check if the "AF_EXAC" key is present in the info_dict
    if "AF_EXAC" not in info_dict:
        return []
    # Check if the Value of "AF_EXAC" is greater than or equal to 0.0001
    if float(info_dict["AF_EXAC"]) >= 0.0001:
        return []   
    
    # Create a list of diseases from the "CLNDN" key in the info_dict
    diseases = info_dict["CLNDN"].split("|")

    # Create a filtered list of diseases
    filtered_diseases = []
    for disease in diseases:
        if disease != "not_provided" and disease != "not_specified":
            filtered_diseases.append(disease)
    
    return filtered_diseases


def read_file(file: str):
    # Dictionary initialization for counting diseases
    tally = {} 
    # open the file
    with open(file) as f: 
        for line in f:
            if (line.startswith("#")):  # filters out metadata lines
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
