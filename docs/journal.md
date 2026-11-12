# Journal de bord

Une entrée par étape : ce qu'on a fait, pourquoi, et les questions que le jury peut poser.
Ce journal sert de base au document de démarche (2 pages) et à la préparation de l'oral.

---

## Étape 0 — Mise en place du projet

**Ce qu'on a fait**
- Arborescence : `data/raw`, `data/processed`, `notebooks`, `src`, `app`, `docs`.
- Environnement virtuel `.venv` + `requirements.txt` avec versions figées.
- `.gitignore` : on exclut `.venv/`, les caches Python/Jupyter et les données.
- Dépôt git initialisé sur la branche `main`.

**Pourquoi**
- Séparer `raw` et `processed` : on ne modifie jamais les données brutes ; tout le nettoyage est refait par script → reproductible.
- Environnement virtuel : les librairies du projet sont isolées de celles du système, et chacun a les mêmes versions.
- On ne versionne pas les données : elles se re-téléchargent avec un script, et git n'est pas fait pour stocker de gros fichiers.

**Questions possibles du jury**
- *Pourquoi un environnement virtuel ?* → Isoler les dépendances et garantir les mêmes versions pour tous.
- *Comment relancer votre projet sur une autre machine ?* → Suivre le README : créer le venv, `pip install -r requirements.txt`, lancer les scripts.
