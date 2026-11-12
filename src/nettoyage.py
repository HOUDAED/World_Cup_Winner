import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_FILE = ROOT / "data" / "raw" / "results.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "matches.csv"


def load() -> pd.DataFrame:
    if not RAW_FILE.exists():
        sys.exit("Erreur : data/raw/results.csv introuvable. Lance d'abord : python -m src.download")
    return pd.read_csv(RAW_FILE)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Corrige les types, retire les lignes inutilisables et trie par date."""
    n_start = len(df)
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")    # texte -> vraie date
    df = df.dropna(subset=["home_score", "away_score"])            # match pas encore joué
    df = df.astype({"home_score": int, "away_score": int})         # scores en nombres entiers
    df = df.drop_duplicates()                                       # lignes en double
    df = df.sort_values("date", kind="stable").reset_index(drop=True)  # ordre chronologique
    print(f"{n_start} matchs au départ, {len(df)} gardés après nettoyage")
    return df


def add_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute l'année, l'écart de buts et le résultat du match."""
    df["year"] = df["date"].dt.year
    df["goal_diff"] = df["home_score"] - df["away_score"]
    df["result"] = "draw"
    df.loc[df["goal_diff"] > 0, "result"] = "home_win"
    df.loc[df["goal_diff"] < 0, "result"] = "away_win"
    return df


def check(df: pd.DataFrame) -> None:
    """Contrôles de cohérence : arrête le programme si une règle n'est pas respectée."""
    if (df["home_score"] < 0).any() or (df["away_score"] < 0).any():
        sys.exit("Erreur : des scores sont négatifs")
    if (df["home_team"] == df["away_team"]).any():
        sys.exit("Erreur : une équipe joue contre elle-même")
    if df["date"].max() > pd.Timestamp.today():
        sys.exit("Erreur : des matchs ont une date dans le futur")
    print("Contrôles OK")


def main() -> None:
    df = load()
    df = clean(df)
    df = add_columns(df)
    check(df)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Enregistré : data/processed/matches.csv ({df['date'].min().date()} -> {df['date'].max().date()})")


if __name__ == "__main__":
    main()
