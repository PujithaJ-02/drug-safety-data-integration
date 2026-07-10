"""
Purpose:
In this file, I define reusable functions that standardize
drug names before matching datasets.
"""


def normalize_drug_name(drug_name):
    """
    Convert a drug name to a standard format.

    Current rules:
    - Convert to lowercase.
    - Remove leading and trailing spaces.
    """

    if drug_name is None:
        return ""

    return str(drug_name).strip().lower()
if __name__ == "__main__":

    print(normalize_drug_name(" BONIVA "))
    print(normalize_drug_name("LYRICA"))
    print(normalize_drug_name(" Ibuprofen "))