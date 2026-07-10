"""
Purpose:
In this file, I load the cleaned openFDA dataset and
the cleaned FDA NDC dataset so they can be matched
in the next steps of the project.
"""

from pathlib import Path

import pandas as pd
from src.utils.normalize import normalize_drug_name


OPENFDA_FILE = Path("data/processed/clean_openfda.csv")
NDC_FILE = Path("data/processed/clean_ndc.csv")


def load_openfda():
    """
    Load cleaned openFDA dataset.
    """
    return pd.read_csv(OPENFDA_FILE)


def load_ndc():
    """
    Load cleaned NDC dataset.
    """
    return pd.read_csv(NDC_FILE)

def exact_match_statistics(openfda_df, ndc_df):
    """
    Compare openFDA drug names against NDC brand and generic names.
    """

    # Unique drug names from openFDA
    openfda_drugs = set(
        openfda_df["event_drug_name"]
        .dropna()
        .apply(normalize_drug_name)
    )

    # Unique brand names
    brand_names = set(
        ndc_df["brand_name"]
        .dropna()
        .apply(normalize_drug_name)
    )

    # Unique generic names
    generic_names = set(
        ndc_df["generic_name"]
        .dropna()
        .apply(normalize_drug_name)
    )

    # Matches
    brand_matches = openfda_drugs.intersection(brand_names)

    generic_matches = openfda_drugs.intersection(generic_names)

    unmatched = openfda_drugs - brand_matches - generic_matches

    print("\n========== Exact Match Summary ==========")
    print(f"Unique openFDA drugs : {len(openfda_drugs)}")
    print(f"Brand matches        : {len(brand_matches)}")
    print(f"Generic matches      : {len(generic_matches)}")
    print(f"Still unmatched      : {len(unmatched)}")

    print("\nMatched by brand name:")
    print(sorted(brand_matches))

    print("\nMatched by generic name:")
    print(sorted(generic_matches))

    print("\nUnmatched drugs:")
    print(sorted(unmatched))
def inspect_drug_in_ndc(drug_name, ndc_df):
    """
    Search the NDC dataset for a drug name.
    """

    print("\n" + "=" * 60)
    print(f"Searching for: {drug_name}")
    print("=" * 60)

    results = ndc_df[
        ndc_df["brand_name"].str.contains(
            drug_name,
            case=False,
            na=False
        )
        |
        ndc_df["generic_name"].str.contains(
            drug_name,
            case=False,
            na=False
        )
    ]

    if results.empty:
        print("No matches found.")
    else:
        print(results[
            [
                "brand_name",
                "generic_name",
                "manufacturer"
            ]
        ].head(10))
def main():

    openfda_df = load_openfda()
    ndc_df = load_ndc()

    print("openFDA Dataset")
    print("----------------")
    print(f"Rows: {len(openfda_df)}")
    print(f"Columns: {len(openfda_df.columns)}")

    print()

    print("NDC Dataset")
    print("----------------")
    print(f"Rows: {len(ndc_df)}")
    print(f"Columns: {len(ndc_df.columns)}")

    # -------------------------------
    # Explore the drug names
    # -------------------------------

    print("\nUnique openFDA drug names:")
    print(openfda_df["event_drug_name"].nunique())

    print("\nUnique NDC brand names:")
    print(ndc_df["brand_name"].nunique())

    print("\nFirst 10 openFDA drug names:")
    print(openfda_df["event_drug_name"].drop_duplicates().head(10))

    print("\nFirst 10 NDC brand names:")
    print(ndc_df["brand_name"].drop_duplicates().head(10))
    exact_match_statistics(openfda_df, ndc_df)
    inspect_drug_in_ndc("boniva", ndc_df)
    inspect_drug_in_ndc("duragesic", ndc_df)
    inspect_drug_in_ndc("talwin", ndc_df)
    inspect_drug_in_ndc("lortab", ndc_df)
    inspect_drug_in_ndc("fiorinal", ndc_df)
    inspect_drug_in_ndc("oxygen", ndc_df)
    inspect_drug_in_ndc("codeine", ndc_df)

if __name__ == "__main__":
    main()