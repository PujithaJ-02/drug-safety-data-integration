import pandas as pd
import matplotlib.pyplot as plt

def main():

    # Load integrated dataset
    df = pd.read_csv("data/processed/integrated_drug_data.csv")

    print("Integrated Dataset")
    print("------------------")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\nColumns:")
    print(df.columns.tolist())
    print("\nDataset Overview")
    print("----------------")

    print("Unique drugs:", df["event_drug_name"].nunique())
    print("Unique reactions:", df["reaction"].nunique())
    print("Unique manufacturers:", df["manufacturer"].nunique())

    print("\nMatch Types")
    print(df["match_type"].value_counts())

    print("\nPatient Sex Distribution")
    print(df["patient_sex"].value_counts(dropna=False))
    print("\nTop 10 Most Reported Drugs")
    print("--------------------------")

    top_drugs = (
        df["event_drug_name"]
        .value_counts()
        .head(10)
    )

    print(top_drugs)
    print("\nTop 10 Most Reported Drugs")
    print("--------------------------")

    top_drugs = (
        df["event_drug_name"]
        .value_counts()
        .head(10)
    )

    print(top_drugs)
    print("\nTop 10 Adverse Reactions")
    print("------------------------")

    top_reactions = (
        df["reaction"]
        .value_counts()
        .head(10)
    )

    print(top_reactions) 
    print("\nTop Manufacturers")
    print("-----------------")

    top_manufacturers = (
        df["manufacturer"]
        .dropna()
        .value_counts()
        .head(10)
    )

    print(top_manufacturers)
    # -----------------------------
    # Top 10 Most Reported Drugs
    # -----------------------------

    top_drugs = (
        df["event_drug_name"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10,6))

    top_drugs.plot(kind="bar")

    plt.title("Top 10 Most Reported Drugs")
    plt.xlabel("Drug")
    plt.ylabel("Number of Reports")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("figures/top_reported_drugs.png")

    plt.close()

    print("\nSaved:")
    print("figures/top_reported_drugs.png")
    # -----------------------------
    # Top 10 Adverse Reactions
    # -----------------------------

    top_reactions = (
        df["reaction"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10,6))

    top_reactions.plot(kind="bar")

    plt.title("Top 10 Adverse Reactions")
    plt.xlabel("Reaction")
    plt.ylabel("Number of Reports")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("figures/top_adverse_reactions.png")

    plt.close()

    print("Saved:")
    print("figures/top_adverse_reactions.png")
    # -----------------------------
    # Match Type Distribution
    # -----------------------------

    match_counts = df["match_type"].value_counts()

    plt.figure(figsize=(7,5))

    match_counts.plot(
        kind="bar"
    )

    plt.title("Drug Matching Method Distribution")
    plt.xlabel("Match Type")
    plt.ylabel("Number of Records")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig("figures/match_type_distribution.png")

    plt.close()

    print("Saved:")
    print("figures/match_type_distribution.png")
    # -----------------------------
    # Top Manufacturers
    # -----------------------------

    top_manufacturers = (
        df["manufacturer"]
        .dropna()
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10,6))

    top_manufacturers.plot(kind="bar")

    plt.title("Top Manufacturers in Drug Reports")
    plt.xlabel("Manufacturer")
    plt.ylabel("Number of Reports")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("figures/top_manufacturers.png")

    plt.close()

    print("Saved:")
    print("figures/top_manufacturers.png")
    # -----------------------------
    # Patient Sex Distribution
    # -----------------------------

    sex_counts = df["patient_sex"].value_counts()

    plt.figure(figsize=(6,5))

    sex_counts.plot(
        kind="bar"
    )

    plt.title("Patient Sex Distribution")
    plt.xlabel("Sex Code")
    plt.ylabel("Number of Reports")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig("figures/patient_sex_distribution.png")

    plt.close()

    print("Saved:")
    print("figures/patient_sex_distribution.png")

if __name__ == "__main__":
    main()