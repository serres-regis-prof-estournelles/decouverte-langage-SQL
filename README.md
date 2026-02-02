# 📊 TD SQLite Géo+

**Travaux dirigés d'apprentissage des bases de données relationnelles avec SQLite et Python**

#

## 📖 Description

Ce projet pédagogique permet d'apprendre à manipuler des bases de données relationnelles à travers l'étude des **données géographiques françaises**.
Les élèves créent une base SQLite contenant **plus de 36 000 villes** et **101 départements**, puis écrivent des **requêtes SQL** et des **scripts Python** pour interroger et analyser ces données.

#

## 🗄️ Structure de la base de données

#

### **Tables principales**

| Table | Description | Nombre d'enregistrements |
|-------|-------------|--------------------------|
| `VILLE` | Informations sur les communes françaises | 36 229 |
| `DEPARTEMENT` | Informations sur les départements | 101 |

#

### **Schéma relationnel**

#

#### **Table VILLE**

- `num_ville` (clé primaire)
- `code_insee`
- `region`
- `nom`
- `nombre`
- `superficie`
- `altitude`
- `canton`
- `codepostal`
- `num_dep` (clé étrangère)

#### **Table DEPARTEMENT**

- `num_dep` (clé primaire)
- `departement`
- `region`
- `chef_lieu`
- `superficie`
- `population`
- `densite`

#

## 🔧 Installation

#

### **Prérequis**

- ✅ **Thonny** pour le langage **PYTHON**
- ✅ **SQLite3** pour LE SGBDR et le **langage SQL**

#

## 📚 Contenu du TD

#

### **Partie 1 : Organisation de la base**

- Identification des tables et clés
- Schéma relationnel
- Types de données (INTEGER, TEXT, REAL)

#

### **Partie 2 : Requêtes SQL**

| Requête | Description |
|---------|-------------|
| `SELECT * FROM VILLE WHERE num_dep=72` | Villes d'un département |
| `WHERE superficie>=35000` | Filtrage par superficie |
| `JOIN` entre tables | Jointure VILLE/DEPARTEMENT |
| `GROUP BY` | Agrégation par région |
| `HAVING` | Filtrage sur agrégats |

#

### **Partie 3 : Scripts Python**

Trois niveaux de scripts d'interrogation :

| Fichier | Niveau | Description |
|---------|--------|-------------|
| `Interroger_villes_enfrance_db01.py` | Débutant | Requêtes de base (COUNT, AVG, MIN) |
| `Interroger_villes_enfrance_db02.py` | Intermédiaire | Requêtes filtrées par région/département |
| `Interroger_villes_enfrance_db03.py` | Avancé | Requêtes complexes avec jointures |

#

## 💻 Exemple d'utilisation

```python
import sqlite3

# Connexion à la base
conn = sqlite3.connect('villes_en_france.db')
cursor = conn.cursor()

# Requête : population par région
cursor.execute('''
    SELECT nom_region, SUM(population) AS population_totale
    FROM DEPARTEMENT
    GROUP BY nom_region
''')

# Affichage formaté
for region, population in cursor.fetchall():
    print(f"{region}: {population:,} habitants")

conn.close()
```

#

## 📁 Jeux de données

| Fichier | Format | Description |
|---------|--------|-------------|
| `VILLE.csv` | CSV | Données des 36 229 communes |
| `DEPARTEMENT.csv` | CSV | Données des 101 départements |
| `DEPARTEMENT.txt` | TXT | Version texte des départements |
| `villes_departements.xlsx` | Excel | Données combinées |

#

## 🎯 Compétences acquises

- Création de tables avec clés primaires et étrangères
- Importation de données CSV
- Requêtes SQL (SELECT, WHERE, ORDER BY, JOIN, GROUP BY, HAVING)
- Utilisation du module `sqlite3` en Python
- Traitement et formatage des résultats


#


👤 Auteur : SERRES Régis Enseignant - Lycée Estournelles de Constant, La Flèche (72) GitHub : @serres-regis-prof-estournelles
