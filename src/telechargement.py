import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pandas as pd

# Adresse de base des fichiers bruts sur GitHub
BASE_URL = "https://raw.githubusercontent.com/martj42/international_results/master/"

FILES = {
    "results.csv": "tous les matchs internationaux depuis 1872",
    "former_names.csv": "anciens noms des pays (ex. Zaïre -> RD Congo)",
    "shootouts.csv": "vainqueurs des séances de tirs au but",
}

RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def download_file(filename: str) -> Path:
    url = BASE_URL + filename
    destination = RAW_DIR / filename
    try:
        with urlopen(url, timeout=30) as response:
            content = response.read()
    except HTTPError as error:
        sys.exit(f"Erreur : le serveur a répondu {error.code} pour {url}")
    except (URLError, TimeoutError) as error:
        sys.exit(f"Erreur : connexion impossible ({error}). Vérifie ta connexion internet puis relance.")

    # On écrit seulement une fois le téléchargement terminé: en cas d'erreur, l'ancien fichier n'est pas écrasé.
    destination.write_bytes(content)
    return destination


def check_file(path: Path) -> None:
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
