BEGIN TRANSACTION;

-- Création de la table 'departements'
CREATE TABLE DEPARTEMENT (
    num_dep TEXT(3) PRIMARY KEY,
    departement TEXT,
    region TEXT,
    chef_lieu TEXT,
    superficie REAL,
    population INTEGER,
    densite REAL
);

-- Importation des données dans la table 'departements' depuis le fichier CSV
.mode csv
.import chemin_vers_departements.csv departements

-- Création de la table 'villes'
CREATE TABLE VILLE (
    num_ville INTEGER PRIMARY KEY,
    code INTEGER,
    insee INTEGER,
    nom TEXT,
    nombre INTEGER,
    superficie REAL,
    altitude INTEGER,
    canton TEXT,
    codepostal INTEGER,
    num_dep TEXT(3),
    FOREIGN KEY (num_dep) REFERENCES departements(num_dep)
);

-- Importation des données dans la table 'villes' depuis le fichier CSV
.mode csv
.import chemin_vers_villes.csv villes

COMMIT;

