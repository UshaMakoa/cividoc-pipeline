# Ajout : test rapide sans régénération

Copiez `quick_test.py` et `test-quick.ps1` à la racine du projet CiviDoc, à côté de `cividoc.py`. Ce mode travaille uniquement sur la sortie existante `generated-user-en/` : il ne fait ni `git clone`, ni `git pull`, ni appel Perplexity/OpenAI, ni nettoyage/réécriture des pages.

## Test rapide complet

```powershell
python .\quick_test.py
```

ou :

```powershell
.\test-quick.ps1
```

Le test vérifie :

- présence et syntaxe de `mkdocs.yml` ;
- présence d'une `nav` non vide et validité de tous ses chemins ;
- dictionnaires de navigation à une seule clé ;
- front matter placé dès le premier caractère de chaque Markdown ;
- champs `categories`, `level`, `summary` et `section` ;
- catégories et niveaux autorisés ;
- présence d'un H1 ;
- commentaires HTML `<!-- -->` équilibrés ;
- absence des anciens `# comment:` ;
- continuité de `part1`, `part2`, `part3`, etc.

Le rapport est écrit dans `generated-user-en/reports/quick_test_report.txt`. Le code de retour vaut `0` si le test réussit et `1` en cas d'erreur, ce qui permet de l'utiliser dans une CI.

## Tester une seule page

```powershell
python .\quick_test.py --page "survey/everyday-tasks-part1.md"
```

C'est le contrôle le plus rapide pendant une correction éditoriale.

## Test avec build incrémental

```powershell
python .\quick_test.py --build
```

Cela ajoute `mkdocs build --dirty`, qui conserve le dossier de sortie et ne reconstruit que ce qui a changé. Pour une validation de production, utilisez plutôt le pipeline complet avec un build propre et strict.

Pour rendre les avertissements MkDocs bloquants durant le test :

```powershell
python .\quick_test.py --build --strict
```

## Tests unitaires uniquement ou combinés

```powershell
python -m unittest discover -s tests -v
python .\quick_test.py --unit
```

## Commandes conseillées

Pendant le travail courant :

```powershell
python .\quick_test.py --page "events/creating-an-event.md"
```

Avant une revue :

```powershell
python .\quick_test.py --build
```

Avant la production :

```powershell
python .\cividoc.py run --ai
```
