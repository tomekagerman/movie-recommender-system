# Movie Recommender System 2.0 Upgrade

This upgrade adds:

- Hybrid recommender module
- Matrix factorization using TruncatedSVD
- Item-item collaborative filtering
- Popularity fallback
- Streamlit app with tabs
- Movie search
- Similar movie search
- User profile and rating system
- Custom recommendations from user ratings
- Simple movie chatbox interface

## Where to put the files

Copy these files into your existing repository:

```text
src/recommender.py
src/user_profiles.py
app/app.py
requirements.txt
```

Your existing processed files should already be here:

```text
data/processed/train.csv
data/processed/val.csv
data/processed/test.csv
data/processed/movies_clean.csv
data/processed/genre_encoded.csv
```

## Install packages

```bash
pip install -r requirements.txt
```

## Run the app

From the root of your repo:

```bash
streamlit run app/app.py
```

## User ratings

The app will create this file automatically:

```text
data/user/user_ratings.csv
```

That file stores custom user profile ratings.
