# Wix Content Intelligence Pipeline

This repository explores the basic approach of **Data Engineering** and **Data Science** tools and principles. It covers extracting **real-world data** (events, articles, blog posts) via API, processing it, and performing analysis.

### Inspiration

The basic idea for this project came from the experiences gathered in the <a href="https://dataklub.hu/" target="_blank" rel="noopener noreferrer">DataKlub</a>.
For the English speaking community, explore this website <a href="https://data36.com/" target="_blank" rel="noopener noreferrer">Data36</a>.

### Main Technologies Used

- **Extraction:** Python (FastAPI), Wix Velo API
- **Processing:** Jupyter Notebook, Pandas
- **Visualization:** Matplotlib, Marp (Presentations)
- **Infrastructure:** Docker, Makefile
- **AI & Automation:** Gemini CLI, pre-commit

> 💡 **Looking for the big picture?**
> Jump straight to the [Data Pipeline Overview](#data-pipeline-overview) to understand the workflow, or view the [Final Presentation](./presentation/presentation.pdf) for a high-level summary of the study's insights.

<br></br>

## Table of Contents

- [Data Pipeline Overview](#data-pipeline-overview)
- [Technical Details](#technical-details)
- [Gemini CLI Integration](#gemini-cli-integration)
- [Jupyter Cleanup & Git Hygiene](#jupyter-cleanup--git-hygiene)
- [Appendix](#appendix)

<br></br>

## Data Pipeline Overview

| Stage          | Process / Service                            | Data State                                     |
| -------------- | -------------------------------------------- | ---------------------------------------------- |
| Source         | **Wix Velo API**                             | Blog posts, Events, Articles (Wix CMS content) |
| Extraction     | **FastAPI / Python**<br>JWT Microservice     | `data_raw/`                                    |
| Transformation | **ETL Layer**<br>(Jupyter Notebook)          | `data_temp/`<br>`data_processed/`              |
| Analysis       | **Data Science Layer**<br>(Jupyter Notebook) | Analysis outputs<br>Models, insights           |
| Presentation   | **Presentation**<br>(Matplotlib)             | Charts, reports, dashboards                    |

<br></br>
![Get Data - Prepare Data - Analyse Data](./assets/data_pipeline_color.png)
<br></br>

### The Underlying Logic

1. **Source of Truth**: Content managed via _Wix_.
2. **Raw Extraction**: _FastAPI_ microservice fetches `JSON` data. For simplicity, this is a _one-time download_ rather than a continuous ingestion pipeline.
3. **Structured Transformation**: Cleaning, normalization, and schema validation.
4. **Interpretation & Insight**: Data analysis.
5. **Presentation**: Conversion of raw numbers into human-consumable insights.

### Data Governance & Directory Mapping

- Data Source — Data was obtained using Wix Velo code during my time as the administrator of the nonprofit organization's [Wix platform](https://www.kiutarakbol.hu/).

- `/data_raw` — Contains the original, unedited dataset. To protect privacy and keep the repo light, this folder is `git-ignored`.

- `/data_raw_dummy` — Tracked by `Git`. Contains representative files with mocked values that match the production schema.

- `/ETL` — Houses the logic for cleaning and validation. This is the "bridge" between raw and processed states

- `/data_temp` — Used for volatile, intermediate states during processing. Not tracked by `Git`.

- `/data_processed` — The final, "science-ready" datasets. Also `git-ignored`.

- `/data_processed_dummy` — Tracked by `Git`. Provides the expected final structure for the analysis.

<br></br>

## Technical Details

This project uses a local-first approach with **Docker**, prioritizing open-source tools and data privacy.

### 📦 Prerequisites

- **[Docker Desktop](https://docs.docker.com/get-docker/)**: For containerizing and running the application.
- **Python 3.x**: (Optional, for local development/testing outside Docker)

### 🖥️ Operating System Used

- Linux Mint 21.2 (development environment used)

### 🐳 Data Extraction (FastAPI Microservice)

This container connects to the **data source (Wix)**, generates a **JWT**, and saves raw **JSON** files locally.

1. ✅ **Configuration** (`.env`)

In the root directory of this project, rename the `.env.example` to `.env`.

Populate the file with your environment keys.

⚠️ **Security Tip:** Never commit your `.env` file to version control.

2. ✅ **Build the Docker Image**

In your terminal, navigate to your project root (where your `Dockerfile.jwt_microservice` and `.env` are located) and run the following command to build the Docker image:

```bash
docker compose build jwt_microservice
```

3. ✅ **Run the Docker Container**

Still in your project root, run the following command to start the Docker container:

```bash
docker compose up -d jwt_microservice
```

This command will start the container in the background (**_detached mode_**), allowing the terminal to be used for `curl` commands.
The additional setting for `jwt_microservice `could be found in the `docker-compose.yml` file.

4. ✅ **Call the Endpoints**

As the container is running in the detached mode, the same terminal could be used to call the endpoints. This triggers

- the microservice to generate a JWT,
- fetch data from Wix, and
- save it locally.

```Bash
# Execute the `curl` Command to Call an Endpoint
curl http://127.0.0.1:8000/events
```

If successful, the downloaded file (e.g., `wix_events_data.json`) will be saved to your project's `/data_raw `directory (relative to your project root).

Available endpoints:

```Bash
# Download events
curl http://127.0.0.1:8000/events

# Download blog posts
curl http://127.0.0.1:8000/blog/posts

# Download blog categories
curl http://127.0.0.1:8000/blog/categories

# Download blog tags
curl http://127.0.0.1:8000/blog/tags

# Download collection with articles
curl http://127.0.0.1:8000/collections/articles

# Download collection with articles' categories
curl http://127.0.0.1:8000/collections/articles-category

# Download members
curl http://127.0.0.1:8000/members
```

5. ✅ **Shut Down the Docker Container**

This container is supposed to run temporary, just for data fetching, which is one time process in this project. When the data is downloaded, shut down the container with this command:

```Bash
docker compose down
```

### 🔬 Data Cleaning & Analysis

Data preparation and analysis are performed using **Jupyter Notebook** and **Pandas**.

The jupyter container in this project uses the recommended [Docker image](https://hub.docker.com/r/jupyter/datascience-notebook/). The additional packages are included inside `requirements_jupyter.txt` file.

1. ✅ **Build the Docker Image**

In your terminal, navigate to your project root (where your `Dockerfile.jupyter` is located) and run the following command to build the Docker image:

```bash
docker compose build jupyter
```

2. ✅ **Run the Docker Container**

Still in your project root, run the following command to start the Docker container:

```bash
docker compose up -d jupyter
```

3. ✅ **Using Dockerized Jupyter**

First, retrieve the Jupyter URL (containing the security **token**) from the container logs:

```bash
docker compose logs jupyter
```

Look for a URL in the terminal output that looks like this:
`http://127.0.0.1:8888/?token=...`

**Option A: Within the Browser** 🌐
Copy the URL above and paste it directly into your web browser. Or hold `Ctrl` (or `Cmd` on Mac) and click the link directly in the terminal.

**Option B: Within VS Code** 💻

1. Open your `.ipynb` file in **VS Code**.
2. Click **_"Select Kernel"_** in the top right corner.
3. Choose **_"Existing Jupyter Server..."_**.
4. Paste the URL you copied from the terminal and press **_Enter_**.

**VS Code** will now connect to the **Docker container**, and you can **_"just code"_** using the packages installed inside Docker!

4. ✅ **Shut Down the Docker Container**

When the data is downloaded, shut down the container with this command:

```Bash
docker compose down
```

<br></br>

## Gemini CLI Integration

This project utilizes the **Gemini CLI** for automating data analysis tasks, generating documentation, and exploring dataset structures.

Prerequisites
Make sure you have the **Gemini CLI** installed and configured on your machine.

[Gemini CLI Documentation](https://geminicli.com/docs/)

### The Tri-File Strategy

Instead of dumping everything into one file, the project documentation was considered in terms of **_Operations_**, **_Truth_**, and **_Persona_**.

#### GEMINI.md (The Operations Manual)

- **_Purpose_**: The **"How-To"** guide for the AI. It explains how to build, test, and maintain the project.
- **_Analogy_**: The Project Manager / Jira
- **_How it works_**: It tells the AI how to interact with the system.

#### CONTEXT.md (The Source of Truth)

- **_Purpose_**: The **"Data & Business Domain"** reference. This file should be the "Database Definition and Project Rules" for the AI.
- **_Analogy_**: The Technical Docs / Schema
- **_How it works_**:
  - **Data Dictionary**: Explain what the JSON keys in your raw data/ folder actually mean.
  - **Schema Definitions**: If you have specific expectations for your data_prepared files, list them.
  - **API Documentation**: A concise summary of your FastAPI endpoints.

#### AGENT.md (The Persona & Standards)

- **_Purpose_**: The **"Guidelines"** for behavior. This is your "**System Prompt**."
  The Senior Mentor / Pair Programmer
- **_Analogy_**: The Senior Mentor / Pair Programmer
- **_How it works_**:
  - **Role**: Define the AI as an "Experienced Data Science Persona."
  - **Code Style**: "Prioritize functional programming, use type hints, and always prefer Pandas vectorized operations over loops."
  - **Constraint Checklist**: "Always verify if a file exists before trying to read it" or "If I ask for a refactor, show me a snippet first, don't rewrite the whole file."

<br></br>

## Jupyter Cleanup & Git Hygiene

> This project uses `nbstripout` to keep notebook outputs out of version control and a `pre-commit` hook to ensure consistent formatting for all files.

- [PyPI: kynan/nbstripout](https://pypi.org/project/nbstripout/)
- [GitHub: kynan/nbstripout](https://github.com/kynan/nbstripout)
- [pre-commit](https://pre-commit.com/)
- [GitHub: pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)

Configuration details can be found in `.pre-commit-config.yaml`.

To check all files and automatically clean notebook outputs before committing, run:

```bash
pre-commit run --all-files
```

### Why `pipx`?

Because `nbstripout` and `pre-commit` are **_development lifecycle tools_**—not dependencies required by the code inside your Docker containers—they are managed via `pipx`.

`pipx` installs Python CLI tools into **_isolated virtual environments_**, keeping your system Python clean while making the binaries globally accessible in your terminal.

[Install pipx](https://pipx.pypa.io/stable/installation/)

```bash
# Install the tools globally, but isolated
pipx install pre-commit
pipx install nbstripout
```

**Note on Environment Strategy:** While these tools could be installed in a local `.venv,` `pipx` is more efficient for "meta-tools." This prevents your project environment from becoming cluttered with tools that aren't needed to run the actual code.
<br></br>

## Appendix

- **Commit Standards**: This project follows [Conventional Commits](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) to maintain a clear and readable history.
- **Presentation**: Insights are delivered using [Marp](https://marp.app/), allowing for a "Presentation-as-Code" workflow that aligns with the Markdown-centric nature of the project.
- **Automation**: A `Makefile` is provided to simplify usual operations.
