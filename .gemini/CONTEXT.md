# Project Context: Wix Data Science Study

## Purpose

This file is the **"Data & Business Domain"** reference. It serves as the Database Definition and Project Rules for the AI.

## Overview

This project extracts raw data from Wix APIs, cleans and prepares it using Jupyter Notebooks, and performs aggregation for Data Science insights.

## Data Structure

- `data_raw/`: Raw JSON dumps directly from API. Ignored from Git.
- `data_raw_dummy/`: Representative files with dummy values matching original schemas. Committed to Git.
- `data_temp/`: Intermediate data during preparation. Ignored by Git, and has no dummy representative for GitHub upload.
- `data_processed/`: Cleaned, structured data ready for analysis. Ignored by Git.
- `data_processed_dummy/`: Cleaned data with dummy values. Committed to Git.
- `ETL/`: Jupyter Notebook files for data preparation.
- `data_science/`: Jupyter Notebook files for data analyses.

## ETL Pipeline Workflow

1. **Extraction**: Run `docker-compose up jwt_microservice` to fetch data from Wix. Raw data lands in `data_raw/`.
2. **Preparation**: Run Jupyter Notebooks in `ETL/` in numerical order to clean raw data.
3. **Storage**: Cleaned data for intermediate use is saved in `data_temp/`, while data ready for Data Science is saved in `data_processed/`.

## Key Files & Roles

- `ETL/`: Shows the thinking process and procedure of data cleaning.
- `data_science/`: Shows the process of data analyses.

## Project Stages

1. Gathering Data
2. Store Data
3. Clean Data
4. Analyse Data
5. Present Data
6. Decisions / Insights for the Future

## Deliverables

- The final output is a short presentation attached to the GitHub repository.

## Data Source

The data is gathered from a Wix platform of a nonprofit organization.
Data types:

- **articles**: Organized in Wix CMS table. Likes/views not supported by API.
- **blog posts**: Regular blog data with metadata (likes, views).
- **events**: Wix Events data.

## Date Formats

- `data_raw/`: `ISO 8601 Combined Date and Time` (e.g., `2025-05-15T09:46:16.031Z`).
- `data_processed/`: `ISO 8601 Calendar Date` (e.g., `2026-01-22`).
- **Processing Rule**: Convert `data_processed/` string dates to actual datetime objects inside Jupyter Notebooks.

## Key Technologies

- Python (FastAPI)
- Jupyter Notebook, Pandas
- Docker
