from pathlib import Path
from urllib.request import urlopen 

import pandas as pd

# Adresse de base des fichiers bruts sur GitHub
BASE_URL = "https://raw.githubusercontent.com/martj42/international_results/master/"

# Fichiers à récupérer, avec leur rôle dans le projet
FILES = {
    "results.csv": "tous les matchs internationaux depuis 1872",
    "former_names.csv": "anciens noms des pays (ex. Zaïre -> RD Congo)",
    "shootouts.csv": "vainqueurs des séances de tirs au but",
}

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def download_file(filename: str) -> Path:
    """Télécharge un fichier depuis la source et l'enregistre dans data/raw/."""
    url = BASE_URL + filename
    destination = RAW_DIR / filename
    with urlopen(url, timeout=30) as response:
        destination.write_bytes(response.read())
    return destination


def check_file(path: Path) -> None:
    """Contrôle rapide : le fichier se lit comme un CSV et n'est pas vide."""
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"{path.name} est vide : le téléchargement a échoué")
    print(f"   -> {len(df)} lignes, {df.shape[1]} colonnes")


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Téléchargement dans {RAW_DIR}")
    for filename, description in FILES.items():
        print(f"- {filename} : {description}")
        path = download_file(filename)
        check_file(path)
    print("Terminé.")


if __name__ == "__main__":
    main()
