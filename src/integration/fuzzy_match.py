import pandas as pd
import os
from rapidfuzz import process, fuzz

from src.utils.normalize import normalize_drug_name


OPENFDA_FILE = "data/processed/clean_openfda.csv"
NDC_FILE = "data/processed/clean_ndc.csv"


def load_data():

    openfda = pd.read_csv(OPENFDA_FILE)
    ndc = pd.read_csv(NDC_FILE)

    return openfda, ndc


def fuzzy_match(drug_name, ndc_names):

    result = process.extractOne(
        drug_name,
        ndc_names,
        scorer=fuzz.token_set_ratio
    )

    return result


def main():

    openfda, ndc = load_data()

    ndc_names = (
    pd.concat(
        [
            ndc["brand_name"],
            ndc["generic_name"],
            ndc["active_ingredient"]
        ]
    )
    .dropna()
    .astype(str)
    .apply(normalize_drug_name)
    .unique()
    .tolist()
    )

    # Remove very short drug names
    ndc_names = [
        name for name in ndc_names
        if len(name) >= 4
    ]
    unmatched_drugs = [
        "boniva",
        "codeine",
        "duragesic",
        "fiorinal",
        "lortab",
        "talwin"
    ]

    matches = []
    for drug in unmatched_drugs:

        normalized = normalize_drug_name(drug)

        match = fuzzy_match(
            normalized,
            ndc_names
        )

        score = match[1]

        if score >= 90:
            decision = "MATCH"

        elif score >= 80:
            decision = "REVIEW"

        else:
            decision = "NO MATCH"

        matches.append(
            {
                "openfda_drug": drug,
                "ndc_candidate": match[0],
                "score": score,
                "decision": decision
            }
        )
    output = pd.DataFrame(matches)
    output.to_csv(
        "data/processed/drug_matches.csv",
        index=False
    )
    print("\nSaved fuzzy matches:")
    print("data/processed/drug_matches.csv")


if __name__ == "__main__":
    main()