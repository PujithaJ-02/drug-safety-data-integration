import pandas as pd

from src.utils.normalize import normalize_drug_name


def main():

    # -----------------------------
    # Load datasets
    # -----------------------------
    openfda_df = pd.read_csv("data/processed/clean_openfda.csv")
    ndc_df = pd.read_csv("data/processed/clean_ndc.csv")
    fuzzy_df = pd.read_csv("data/processed/drug_matches.csv")

    print(f"openFDA records: {len(openfda_df)}")
    print(f"NDC records: {len(ndc_df)}")
    print(f"Fuzzy matches: {len(fuzzy_df)}")

    # -----------------------------
    # Normalize drug names
    # -----------------------------
    openfda_df["join_name"] = openfda_df["event_drug_name"].apply(
        normalize_drug_name
    )

    ndc_df["brand_join"] = ndc_df["brand_name"].apply(
        normalize_drug_name
    )

    ndc_df["generic_join"] = ndc_df["generic_name"].apply(
        normalize_drug_name
    )

    # -----------------------------
    # Keep one NDC row per drug
    # -----------------------------
    ndc_brand = ndc_df.drop_duplicates(subset="brand_join")
    ndc_generic = ndc_df.drop_duplicates(subset="generic_join")

    # -----------------------------
    # Brand merge
    # -----------------------------
    integrated = openfda_df.merge(
        ndc_brand[
            [
                "brand_join",
                "brand_name",
                "generic_name",
                "manufacturer",
                "dosage_form",
                "route",
            ]
        ],
        left_on="join_name",
        right_on="brand_join",
        how="left",
    )

    integrated["match_type"] = None
    integrated.loc[
        integrated["brand_name"].notna(),
        "match_type",
    ] = "Brand"

    # -----------------------------
    # Generic merge
    # -----------------------------
    generic_lookup = ndc_generic[
        [
            "generic_join",
            "brand_name",
            "generic_name",
            "manufacturer",
            "dosage_form",
            "route",
        ]
    ]

    generic_lookup = generic_lookup.rename(
        columns={
            "brand_name": "g_brand_name",
            "generic_name": "g_generic_name",
            "manufacturer": "g_manufacturer",
            "dosage_form": "g_dosage_form",
            "route": "g_route",
        }
    )

    integrated = integrated.merge(
        generic_lookup,
        left_on="join_name",
        right_on="generic_join",
        how="left",
    )

    # Fill missing values using generic matches
    for col in [
        "brand_name",
        "generic_name",
        "manufacturer",
        "dosage_form",
        "route",
    ]:
        integrated[col] = integrated[col].fillna(
            integrated["g_" + col]
        )

    integrated.loc[
        (integrated["match_type"].isna())
        & (integrated["generic_name"].notna()),
        "match_type",
    ] = "Generic"

    # -----------------------------
    # Fuzzy matches
    # -----------------------------
    fuzzy_lookup = fuzzy_df[
        fuzzy_df["decision"] == "MATCH"
    ][["openfda_drug", "ndc_candidate"]]

    fuzzy_lookup["openfda_drug"] = fuzzy_lookup[
        "openfda_drug"
    ].apply(normalize_drug_name)

    fuzzy_dict = dict(
        zip(
            fuzzy_lookup["openfda_drug"],
            fuzzy_lookup["ndc_candidate"],
        )
    )

    integrated.loc[
        integrated["match_type"].isna()
        & integrated["join_name"].isin(fuzzy_dict.keys()),
        "match_type",
    ] = "Fuzzy"

    # -----------------------------
    # Remaining records
    # -----------------------------
    integrated["match_type"] = integrated["match_type"].fillna(
        "Unmatched"
    )

    # -----------------------------
    # Keep useful columns
    # -----------------------------
    final_df = integrated[
        [
            "event_drug_name",
            "reaction",
            "reaction_outcome",
            "patient_sex",
            "drug_indication",
            "brand_name",
            "generic_name",
            "manufacturer",
            "dosage_form",
            "route",
            "match_type",
        ]
    ]

    # -----------------------------
    # Save dataset
    # -----------------------------
    final_df.to_csv(
        "data/processed/integrated_drug_data.csv",
        index=False,
    )

    print("\nIntegrated Dataset Created")
    print("--------------------------")
    print("Rows:", len(final_df))
    print("Columns:", len(final_df.columns))

    print("\nMatch Summary")
    print(final_df["match_type"].value_counts())
    print("\nUnique drugs by match type")
    print(
        final_df.groupby("match_type")["event_drug_name"]
        .nunique()
    )

    print("\nSaved to:")
    print("data/processed/integrated_drug_data.csv")


if __name__ == "__main__":
    main()