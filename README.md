
# TEKNOFEST E-Commerce Datathon (Aug 8–22, 2025)


**Collaboration Guidelines:**
- Do not commit directly to the `main` branch.
- Each team member should create a separate branch for their work (e.g., `feature/your-name-eda`, `feature/modeling`, etc.).
- After making changes, open a merge request (pull request) to merge your branch into `main`.
- Review and discuss code in merge requests before merging.

**Important:**
- Never push model files, result outputs, or any large/generated artifacts (e.g., files in `models/`, `results/`, or raw data) to the repository. These are ignored by `.gitignore` and should remain local.
- Note: The `models/` and `results/` folders are always present locally (with a `.gitkeep` file), but GitHub may not display them in the UI if they are completely empty. As soon as you add a tracked file (like `.gitkeep`), they should appear, but sometimes GitHub's UI may still hide them until another file is added.

## Overview
Predict clicked and purchased products per session. Evaluation is based on weighted Recall@K (click + purchase).

## Project Structure
```
ecommerce-datathon/
├── notebooks/          # EDA + Kaggle experiments
├── data/raw/           # Provided data (excluded from git)
├── data/processed/     # Feature tables
├── models/             # Saved model artifacts
├── results/            # Predictions + scores
├── src/data/           # Data loaders
├── src/features/       # Feature engineering
├── src/models/         # Model training + inference
├── src/evaluation/     # Metrics (recall@k)
├── scripts/            # CLI scripts for train/infer/submit
├── requirements.txt
└── README.md
```


## Setup
```bash
pip install -r requirements.txt
```

## Data Handling

- **Raw competition data (~5 GB) must be placed in `data/raw/` and is excluded from GitHub via `.gitignore`.**
- Team members should download the dataset locally using either:
  1. **Manual download from Kaggle** and move files to `data/raw/`.
  2. **Kaggle CLI:**
     ```bash
     pip install kaggle
     mkdir -p ~/.kaggle
     cp kaggle.json ~/.kaggle/
     chmod 600 ~/.kaggle/kaggle.json
     kaggle competitions download -c <competition-name> -p data/raw
     unzip data/raw/*.zip -d data/raw
     ```
- For exploration, load only a sample with:
  ```python
  import pandas as pd
  df = pd.read_csv("data/raw/train.csv", nrows=200_000)
  ```
- **Do not commit raw data to Git; `.gitignore` already prevents it.**
- Keep heavy EDA on local machines; push only lightweight processed samples to `data/processed/`.

## Usage
- **EDA & Experiments:**
  - Use Jupyter notebooks in `notebooks/` for exploration and Kaggle submissions.
- **Train Model:**
  - Example: `python scripts/train.py`
- **Generate Submission:**
  - Example: `python scripts/generate_submission.py`

## Data
- Place provided data in `data/raw/` (excluded from git).
- Processed features will be saved in `data/processed/`.

## Scripts
- `scripts/generate_submission.py`: Dummy popularity-based submission generator.

## Source Code
- `src/data/`: Data loading utilities.
- `src/features/`: Feature engineering.
- `src/models/`: Model training and inference.
- `src/evaluation/`: Evaluation metrics (recall@k).

## Requirements
See `requirements.txt` for dependencies.
