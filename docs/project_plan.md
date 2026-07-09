# Project Plan

## Project Name

Drug Safety Data Integration

## Goal

Build a clean analytics dataset by combining drug event data from the openFDA API with a public drug reference dataset.

## Data Sources

Source 1
- openFDA Drug Event API

Source 2
- FDA National Drug Code (NDC) Directory

## Main Tasks

- Understand both datasets
- Download data
- Clean each dataset
- Match drugs between the datasets
- Merge into one dataset
- Validate the merged data
- Explore the final dataset

## Status

Project started.
## Source 1 Notes

Observations

- The API returns JSON data.
- One report contains patient information.
- Each report can contain one or more drugs.
- Each report can contain one or more reactions.
- Drug information is nested inside the patient object.