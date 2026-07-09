"""
Purpose:
In this file, I read raw openFDA JSON files,
extract important drug safety event information,
and create a clean dataset for future integration.
"""

from pathlib import Path
import json

import pandas as pd


# Folder containing raw openFDA JSON files
RAW_API_FOLDER = Path("data/raw/api")

# Output file for cleaned openFDA data
OUTPUT_FILE = Path("data/processed/clean_openfda.csv")


def extract_drug_events():
    """
    Read all openFDA JSON files and extract useful fields.
    """

    records = []

    # Read every JSON file inside the API folder
    for json_file in RAW_API_FOLDER.glob("*.json"):

        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Each JSON file contains a list of reports
        for report in data.get("results", []):

            patient = report.get("patient", {})

            # Extract reactions
            reactions = patient.get("reaction", [])

            # Extract drugs
            drugs = patient.get("drug", [])

            # Extract manufacturer information
            manufacturers = report.get("primarysource", {}).get(
                "reportercountry", ""
            )

            # If there are multiple reactions, capture each one
            for reaction in reactions:

                # If there are multiple drugs, capture each one
                for drug in drugs:

                    records.append(
                        {
                            "event_drug_name": drug.get(
                                "medicinalproduct", ""
                            ),
                            "drug_characterization": drug.get(
                                "drugcharacterization", ""
                            ),
                            "drug_authorization_number": drug.get(
                                "drugauthorizationnumb", ""
                            ),
                            "drug_route_code": drug.get(
                                "drugadministrationroute", ""
                            ),
                            "drug_indication": drug.get(
                                "drugindication", ""
                            ),
                            "reaction": reaction.get(
                                "reactionmeddrapt", ""
                            ),
                            "reaction_outcome": reaction.get(
                                "reactionoutcome", ""
                            ),
                            "patient_sex": patient.get(
                                "patientsex", ""
                            ),
                            "source_file": json_file.name
                        }
                    )

    return pd.DataFrame(records)


def main():
    """
    Clean openFDA data and save as CSV.
    """

    df = extract_drug_events()

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("openFDA dataset cleaned successfully")
    print("--------------------------------")
    print(f"Records created: {len(df)}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()