"""
Purpose:
In this file, I read the raw FDA NDC product dataset,
select useful drug product fields, clean the data,
and create a standardized dataset for integration.
"""

from pathlib import Path

import pandas as pd


# Raw NDC dataset location
RAW_NDC_FILE = Path("data/raw/ndc/product.xls")

# Cleaned output location
OUTPUT_FILE = Path("data/processed/clean_ndc.csv")


def clean_text(value):
    """
    Standardize text values for easier matching.
    """

    if pd.isna(value):
        return ""

    return (
        str(value)
        .lower()
        .strip()
    )


def load_ndc_data():
    """
    Load raw NDC tab-separated dataset.
    """

    df = pd.read_csv(
        RAW_NDC_FILE,
        sep="\t",
        encoding="latin-1"
    )

    return df


def clean_ndc_data(df):
    """
    Select and clean important NDC columns.
    """

    selected_columns = [
        "PRODUCTNDC",
        "PROPRIETARYNAME",
        "NONPROPRIETARYNAME",
        "LABELERNAME",
        "SUBSTANCENAME",
        "DOSAGEFORMNAME",
        "ROUTENAME",
        "STARTMARKETINGDATE"
    ]

    df = df[selected_columns].copy()

    # Rename columns for easier use
    df = df.rename(
        columns={
            "PRODUCTNDC": "ndc_product_id",
            "PROPRIETARYNAME": "brand_name",
            "NONPROPRIETARYNAME": "generic_name",
            "LABELERNAME": "manufacturer",
            "SUBSTANCENAME": "active_ingredient",
            "DOSAGEFORMNAME": "dosage_form",
            "ROUTENAME": "route",
            "STARTMARKETINGDATE": "start_marketing_date"
        }
    )

    # Clean text fields
    text_columns = [
        "brand_name",
        "generic_name",
        "manufacturer",
        "active_ingredient",
        "dosage_form",
        "route"
    ]

    for column in text_columns:
        df[column] = df[column].apply(clean_text)

    # Create matching column
    df["clean_drug_name"] = df["brand_name"]

    return df


def main():
    """
    Execute NDC cleaning pipeline.
    """

    raw_df = load_ndc_data()

    clean_df = clean_ndc_data(raw_df)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    clean_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("NDC dataset cleaned successfully")
    print("--------------------------------")
    print(f"Records created: {len(clean_df)}")
    print(f"Columns created: {len(clean_df.columns)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()