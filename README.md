# CiviDoc pipeline

Projet Python unique pour récupérer la documentation officielle CiviCRM, la réécrire facultativement avec une IA, préparer MkDocs, conserver la navigation officielle, gérer les pages `part1`, `part2`, etc., générer les catégories, auditer Diátaxis et construire le site.

## Ce que fait une exécution

1. Clone `https://lab.civicrm.org/documentation/docs/user-en.git`, ou exécute `git pull --ff-only` si le dépôt est déjà présent.
2. Utilise **le `mkdocs.yml` du dépôt officiel courant** comme modèle, notamment sa `nav` et son ordre.
3. Avec `--ai`, réécrit les fichiers Markdown à partir des sources Git, avec cache et reprise automatique.
4. Copie le dépôt officiel dans un dossier de sortie sans toucher au clone amont, puis superpose les pages réécrites.
5. Garantit un front matter en première ligne, normalise `categories`, `level`, `summary`, `section`, les commentaires HTML et les listes aplaties.
6. Si `page-part1.md`, `page-part2.md`, etc. existent, supprime `page.md`, remplace son lien de nav par `part1`, puis insère les autres parties juste dessous dans l'ordre numérique.
7. Retire de la nav les références qui n'existent plus, sans perdre les entrées titrées.
8. Conserve et configure `mkdocs-categories-plugin`.
9. Produit un audit Diátaxis dans `generated-user-en/reports/` sans l'ancien avertissement sur les conclusions.
10. Lance `mkdocs build --strict`; avec `--serve`, ouvre ensuite le serveur local.

## Prérequis

- Python 3.10 ou supérieur.
- Git disponible dans `PATH`.
- Une clé API uniquement si `--ai` est utilisé.

Sous PowerShell :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Renseignez `PERPLEXITY_API_KEY` dans `.env` si la réécriture IA est activée. Le script lit bien `PERPLEXITY_API_KEY`, et non l'ancien nom erroné `PERPLEXITY_API_NAME`.

## Une seule commande

Pipeline complet avec Perplexity, build strict et serveur local :

```powershell
python .\cividoc.py run --ai --fresh --serve
```

Le premier traitement intégral peut générer beaucoup d'appels API. Testez d'abord sur deux pages :

```powershell
python .\cividoc.py run --ai --include events --limit 2 --skip-build
```

Sans IA, pour valider immédiatement le pipeline sur la documentation officielle :

```powershell
python .\cividoc.py run --fresh --serve
```

Le site local est normalement visible sur `http://127.0.0.1:8000/`.

## Reprise et cache

Après la première exécution, omettez `--fresh`. Le dépôt officiel sera mis à jour et les pages IA inchangées seront lues depuis le cache :

```powershell
python .\cividoc.py run --ai --serve
```

Dossiers créés :

```text
.cividoc/
  upstream-user-en/     clone officiel, jamais modifié
  rewritten-docs/      sorties IA
  state/               manifeste de cache
generated-user-en/     site MkDocs final
  docs/
  reports/
  mkdocs.yml
```

## Commandes séparées

```powershell
python .\cividoc.py sync
python .\cividoc.py build
python .\cividoc.py serve
```

## Traduction dynamique facultative

Pour injecter le sélecteur LibreTranslate sans override du header ou du footer :

```powershell
python .\cividoc.py run --translator-url "https://translate.example.org/translate" --serve
```

Le script crée `docs/js/libretranslate-selector.js` et l'ajoute à `extra_javascript`. N'insérez jamais une clé privée dans ce JavaScript : utilisez une instance sans clé ou un proxy côté serveur. L'endpoint doit autoriser CORS et accepter `q` sous forme de tableau. Le sélecteur propose anglais, français, italien, néerlandais, espagnol et catalan.

## Publication

Avant production :

```powershell
python .\cividoc.py run --ai
cd generated-user-en
git diff --check
python -m mkdocs build --strict
```

Relisez les changements, les rapports, les liens, les tables et quelques pages de chaque type Diátaxis. La sortie `generated-user-en/` est volontairement indépendante du clone officiel afin d'éviter tout écrasement accidentel.
