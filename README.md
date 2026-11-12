# WORLD CUP WINNER — Qui va gagner la Coupe du monde 2030 ?

Projet de machine learning de 9 jours (sujet 2).

**Question :** une équipe nationale va-t-elle gagner son match ?
On entraîne un modèle sur ~50 000 matchs internationaux depuis 1872, puis on s'en sert pour pronostiquer la Coupe du monde 2030.

## Données

- Source : [martj42/international_results](https://github.com/martj42/international_results) (libre accès)
- Les données sont **téléchargées automatiquement** par un script, elles ne sont pas versionnées dans git.

## Installation

```bash
git clone https://github.com/HOUDAED/World_Cup_Winner.git
cd World_Cup_Winner
python3 -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer le projet

> À compléter au fil des étapes (téléchargement, entraînement, dashboard).

## Arborescence

```
World_Cup_Winner/
├── data/
│   ├── raw/          # données brutes téléchargées (jamais modifiées à la main)
│   └── processed/    # données nettoyées produites par nos scripts
├── notebooks/        # exploration des données (graphiques commentés)
├── src/              # code Python : téléchargement, nettoyage, features, modèles
├── app/              # dashboard Streamlit
├── docs/             # document de démarche, journal de bord
├── requirements.txt  # librairies et versions exactes
└── README.md
```

## Équipe et rôles

Chaque membre pilote une partie, mais tout le monde doit savoir expliquer l'ensemble du projet.

| Rôle | Membre | Responsable de |
|---|---|---|
| Data Engineer | Edvige | Collecte, nettoyage, variables (forme récente, lieu, Elo), pipeline, git |
| Data Analyst | Kerem | Notebook d'exploration, dashboard Streamlit, support de soutenance |
| Data Scientist | Quochuy | Modèle naïf, modèles de ML, validation, simulation 2030 |
