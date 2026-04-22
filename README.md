[README.md](https://github.com/user-attachments/files/26989879/README.md)
# Movie Recommender Upgrade Pack

This package includes:

- `notebooks/03_matrix_factorization_upgraded.ipynb`
- `src/recommender.py`
- `app/app.py`
- `requirements.txt`

## What changed

### 1) Matrix Factorization
Added a `TruncatedSVD`-based recommender to learn latent user/movie factors.

### 2) Hybrid Recommender
The final score combines:

- collaborative filtering score
- matrix factorization score
- genre overlap score
- popularity fallback score

### 3) Deployable App
A Streamlit app is included. It supports:
- recommendations by user ID
- similar movies search
- popularity fallback
- poster fetching with TMDb API
- hover cards with title context and explanation

## Recommended repo layout

```text
movie-recommender-system/
├── app/
│   └── app.py
├── data/
│   └── processed/
├── models/
├── notebooks/
├── src/
│   └── recommender.py
└── requirements.txt
```

## How to install

```bash
pip install -r requirements.txt
```

## How to run locally

```bash
streamlit run app/app.py
```

## How to deploy on Streamlit Community Cloud

1. Push your repo to GitHub
2. Make sure these files exist:
   - `app/app.py`
   - `requirements.txt`
   - `src/recommender.py`
3. In Streamlit Cloud, choose:
   - repo: your GitHub repo
   - main file path: `app/app.py`
4. Optional: add `TMDB_API_KEY` as a secret for posters

## Environment variable for posters

Set:

```bash
export TMDB_API_KEY=your_key_here
```

Without this key, the app still works but shows placeholder poster cards.
