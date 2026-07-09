"""
Purpose:
In this file, I load the raw FDA NDC product dataset,
read the NDC tab-separated file, and inspect the dataset structure.
"""

from pathlib import Path

import pandas as pd


# Location of the raw NDC dataset
NDC_FILE = Path("data/raw/ndc/product.xls")


def load_ndc_data():
    """
    Load the NDC Excel file into a Pandas DataFrame.
    """

    # Read Excel file
    df = pd.read_csv(NDC_FILE, sep="\t", encoding="latin-1")

    return df


def main():
    """
    Load NDC data and display basic information.
    """

    ndc_df = load_ndc_data()

    print("NDC dataset loaded successfully")
    print("--------------------------------")

    print(f"Number of rows: {len(ndc_df)}")
    print(f"Number of columns: {len(ndc_df.columns)}")

    print("\nColumns:")
    print(ndc_df.columns.tolist())

    print("\nFirst 5 rows:")
    print(ndc_df.head())


if __name__ == "__main__":
    main()