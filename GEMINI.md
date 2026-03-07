# GEMINI.md - Operations Manual

This document provides instructions for building, running, and maintaining the **Data Science & Engineering Study Project**.

## Project Overview

This project is a Data Science study that extracts raw data from Wix APIs, processes it via an ETL pipeline, and performs analysis. It uses a local-first approach with Docker, prioritizing open-source tools and data privacy.

### Core Technologies

- **Languages:** Python 3.10+ (FastAPI, Pandas)
- **Infrastructure:** Docker & Docker Compose
- **Data Engineering:** Jupyter Notebooks
- **Workflow Tools:** `pre-commit`, `nbstripout` (for notebook cleaning)

---

## Building and Running

### 1. Data Extraction (FastAPI Microservice)

This service fetches data from Wix and saves it as raw JSON files in `data_raw/`.

- **Setup:** Rename `.env.example` to `.env` and fill in Wix API credentials.
- **Build:** `docker compose build jwt_microservice`
- **Run:** `docker compose up -d jwt_microservice`
- **Fetching Data:** Use `curl` to trigger endpoints:
  - `curl http://127.0.0.1:8000/events` (Events)
  - `curl http://127.0.0.1:8000/blog/posts` (Blog Posts)
  - `curl http://127.0.0.1:8000/blog/categories` (Blog Categories)
  - `curl http://127.0.0.1:8000/blog/tags` (Blog Tags)
  - `curl http://127.0.0.1:8000/collections/articles` (Articles)
  - `curl http://127.0.0.1:8000/collections/articles-category` (Article Categories)
  - `curl http://127.0.0.1:8000/members` (Members)

### 2. Data Cleaning & Analysis (Jupyter)

ETL and Analysis are performed inside a Jupyter environment.

- **Build:** `docker compose build jupyter`
- **Run:** `docker compose up -d jupyter`
- **Access:** Check logs for the token: `docker compose logs jupyter`.
- **VS Code Integration:** Use the "Existing Jupyter Server" option with the tokenized URL.

### 3. ETL Pipeline Execution Order

Notebooks in `ETL/` should be run in numerical order:

1. `1_prepare_articles_data.ipynb`
2. `2_1_prepare_blog_posts_data_intermediate.ipynb`
3. `2_2_prepare_blog_posts_data_authors.ipynb`
4. `3_1_prepare_events_data.ipynb`
5. `3_2_prepare_events_data_speakers_intermediate.ipynb`
6. `3_3_prepare_events_data_category.ipynb`
7. `3_4_prepare_events_data_speakers.ipynb`

Processed data is saved in `data_processed/`.

---

## Development Conventions

### Coding Style

- **Python:** Use type hints where possible (especially in FastAPI).
- **Pandas:** Prioritize vectorized operations over loops.
- **Notebooks:** Use Markdown cells to explain the "why" behind data transformations.

### Data Privacy & Git Hygiene

- **Raw Data:** Never commit files in `data_raw/` or `data_processed/`. Use `data_raw_dummy/` and `data_processed_dummy/` for representative data.
- **Environment:** Never commit `.env`.
- **Notebooks:** Always use `nbstripout` to clear cell outputs before committing.
- **Pre-commit:** Run `pre-commit run --all-files` before pushing changes.

### File Structure

- `data_get/`: FastAPI microservice and Velo code.
- `data_raw/`: Input JSON files from Wix API.
- `data_temp/`: Intermediate data files during ETL.
- `data_processed/`: Cleaned, analysis-ready data.
- `ETL/`: Cleaning and normalization notebooks.
- `data_science/`: Analysis notebooks.

---

## Common Commands Recap

- Start Docker Desktop

```bash
docker desktop start
```

- Stop Docker Desktop

```bash
docker desktop stop
```

- Build the Docker Image for the JWT Microservice

```bash
docker compose build jwt_microservice
```

- Start the Docker Container for JWT Microservice

```bash
docker compose up -d jwt_microservice
```

- Build the Docker Image for Jupyter

```bash
docker compose build jupyter
```

- Start the Docker Container for Jupyter

```bash
docker compose up -d jupyter
```

- Extract the Jupyter Token

```bash
docker compose logs jupyter
```

- Stop the Docker Container

```bash
docker compose down
```

- Remove JWT Microservice Image

```bash
docker rmi jwt microservice
```

- Remove Jupyter Image

```bash
docker rmi jupyter
```

- Run pre-commit Checks

```bash
pre-commit run --all-files
```

---

## Shortcuts for Gemini CLI

| Shortcut      | Command                                                                                   |
| :------------ | :---------------------------------------------------------------------------------------- |
| **`d start`** | `docker desktop start && sleep 5 && until docker info > /dev/null 2>&1; do sleep 2; done` |
| **`d stop`**  | `docker desktop stop`                                                                     |
| **`b jwt`**   | `docker compose build jwt_microservice`                                                   |
| **`up jwt`**  | `docker compose up -d jwt_microservice`                                                   |
| **`b jup`**   | `docker compose build jupyter`                                                            |
| **`up jup`**  | `docker compose up -d jupyter`                                                            |
| **`token`**   | `docker compose logs jupyter`                                                             |
| **`down`**    | `docker compose down`                                                                     |
| **`pc`**      | `pre-commit run --all-files`                                                              |
