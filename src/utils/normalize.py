"""
Purpose:
In this file, I define reusable functions that standardize
drug names before matching datasets.
"""
import string
import re

def normalize_drug_name(drug_name):
    """
    Convert a drug name to a standard format.

    Current rules:
    - Convert to lowercase.
    - Remove leading and trailing spaces.
    """

    if drug_name is None:
        return ""

    name = str(drug_name).strip().lower()
    name = name.translate(str.maketrans("", "", string.punctuation))
    name = re.sub(r"(?<=[a-z]{4})\d+$", "", name)
    return name
if __name__ == "__main__":

    #print(normalize_drug_name(" BONIVA "))
    #print(normalize_drug_name("LYRICA"))
    #print(normalize_drug_name(" Ibuprofen "))
    #print(normalize_drug_name("oxygen."))
    #print(normalize_drug_name("DURAGESIC-100"))
    print(normalize_drug_name("DURAGESIC-100"))
    print(normalize_drug_name("OXYCONTIN10"))
    print(normalize_drug_name("B12"))