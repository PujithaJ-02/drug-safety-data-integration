# Drug Safety Data Integration & Adverse Event Analysis

## Project Overview

I built this project to combine drug safety data with official drug product information and create a cleaner dataset for analysis.

The project integrates adverse drug event reports from the openFDA API with drug information from the FDA National Drug Code (NDC) database.

The main goal of this project was to build a pipeline that can clean drug data, match drugs between different datasets, and analyze adverse drug reactions.

---

## Problem

Drug names are not always stored in the same format across different datasets.

For example:

- DURAGESIC-100
- Duragesic
- duragesic

These names refer to the same drug, but simple matching methods may not identify them as the same.

To solve this problem, I created a drug matching process using:

- Brand name matching
- Generic name matching
- Fuzzy string matching

---

## Data Sources

### openFDA Drug Safety API

Source:
https://open.fda.gov/apis/

The dataset contains:

- Drug names
- Adverse reactions
- Patient information
- Drug indications
- Drug outcomes


### FDA National Drug Code (NDC) Directory

Source:
https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory

The dataset contains:

- Brand names
- Generic names
- Manufacturers
- Dosage forms
- Routes of administration

---

# Project Pipeline

1. Data Collection

Collected drug safety information from openFDA and drug product information from the FDA NDC database.


2. Data Cleaning

Cleaned and prepared the datasets by:

- Removing unnecessary columns
- Handling missing values
- Standardizing column names
- Preparing drug information for matching


3. Drug Name Normalization

Created a normalization process to handle differences in drug names.

The process includes:

- Converting names to lowercase
- Removing extra spaces
- Removing unnecessary characters
- Handling different naming formats


4. Drug Matching

Matched drugs between openFDA and NDC datasets using:

Brand Name Matching:
- Matches drugs using brand names.

Generic Name Matching:
- Matches drugs using generic names.

Fuzzy Matching:
- Uses similarity scores to find possible matches when exact matching fails.


5. Integrated Dataset Creation

Combined drug safety information with NDC drug details.

The final dataset contains:

- Drug information
- Adverse reactions
- Manufacturer details
- Dosage information
- Route information
- Match type


6. Exploratory Data Analysis

Analyzed the integrated dataset to understand:

- Most reported drugs
- Common adverse reactions
- Manufacturers
- Drug matching performance


7. Visualization

Created charts to visualize:

- Top reported drugs
- Top adverse reactions
- Drug matching results
- Top manufacturers
- Patient distribution

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- RapidFuzz
- openFDA API
- Git and GitHub

---

# Project Structure

drug-safety-data-integration

data

- raw
- processed


src

- cleaning
    - clean_openfda.py
    - clean_ndc.py

- integration
    - match_drugs.py
    - fuzzy_match.py
    - create_integrated_dataset.py

- analysis
    - exploratory_analysis.py

- utils
    - normalize.py


figures

- Analysis visualization images


requirements.txt

README.md

---

# Drug Matching Approach

## Brand Name Matching

First, I matched drugs using brand names.

Example:

openFDA:

LYRICA

NDC:

lyrica

Result:

Matched


---

## Generic Name Matching

If brand matching was not successful, I compared generic drug names.

Example:

openFDA:

IBUPROFEN

NDC:

ibuprofen

Result:

Matched


---

## Fuzzy Matching

Some drugs had different names between datasets.

For these cases, I used RapidFuzz to calculate similarity scores.

Example:

openFDA:

CODEINE

NDC:

codeine sulfate

Similarity Score:

100%

Result:

Matched

---

# Dataset Results

After creating the integrated dataset:

Total Records:

74


Unique Drugs:

22


Unique Reactions:

16


Unique Manufacturers:

14


---

# Drug Matching Results

Brand Matches:

52 records


Generic Matches:

2 records


Fuzzy Matches:

2 records


Unmatched:

18 records


---

# Exploratory Analysis Results

The analysis showed:

- LETAIRIS had the highest number of reports in this dataset.
- Drug hypersensitivity was the most common adverse reaction.
- Most successful matches came from brand name matching.
- Manufacturer information was successfully added from the NDC database.

---

# Visualizations

The project includes visualizations for:

- Top reported drugs
- Most common adverse reactions
- Drug matching distribution
- Top manufacturers
- Patient distribution


---

# How to Run the Project

Clone the repository:

git clone <repository-url>


Install dependencies:

pip install -r requirements.txt


Create integrated dataset:

python3 -m src.integration.create_integrated_dataset


Run analysis:

python3 -m src.analysis.exploratory_analysis


---

# What I Learned

Through this project, I learned how to:

- Work with real-world healthcare datasets
- Build a complete data integration pipeline
- Clean and transform raw data
- Handle inconsistent drug names
- Apply fuzzy matching techniques
- Perform exploratory data analysis
- Create meaningful visualizations


---

# Future Improvements

Some improvements I would like to add:

- Use larger healthcare datasets
- Improve matching accuracy with machine learning approaches
- Add automated pipeline scheduling
- Build an interactive dashboard using Tableau or Power BI
- Perform deeper adverse event analysis