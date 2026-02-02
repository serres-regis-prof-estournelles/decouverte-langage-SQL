import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('villes_en_france.db')
cursor = conn.cursor()


# Requête 1 : Compter le nombre total de villes dans la base de données
cursor.execute('''
    SELECT COUNT(*) FROM VILLE
    WHERE num_dep=72
''')
resultat_1 = cursor.fetchone()
print("Requête 1 : Nombre total de villes dans la Sarthe")
print(resultat_1[0]," villes en Sarthe")
print()


# Requête 2 : Calculer la moyenne de la population des villes des Pays de la Loire
cursor.execute('''
    SELECT AVG(nombre) FROM VILLE
    WHERE num_dep=72 or num_dep=49 or num_dep=53 or num_dep=44 or num_dep=85
''')
resultat_2 = cursor.fetchone()
print("Requête 2 : Moyenne de la population des villes des Pays de la Loire")
print(resultat_2[0]*1000," habitants")
print()
resultat_2 = cursor.fetchall()

# Affichage des résultats sans parenthèses ni apostrophes
for resultat in resultat_2:
    print(resultat[0], ": ", resultat[1], " habitants au km2")

print()


# Requête 3 : Sélectionner les départements avec une superficie totale supérieure à 650 000 km2
cursor.execute('''
    SELECT D.nom_dep, SUM(V.superficie) AS superficie_totale
    FROM VILLE V
    JOIN DEPARTEMENT D ON V.num_dep = D.num_dep
    GROUP BY V.num_dep
    HAVING superficie_totale > 650000
    AND nom_region = 'Pays de la Loire'
''')
resultat_3 = cursor.fetchall()
print("Requête 3 : Départements avec une superficie totale supérieure à 650 000 km2")
print(resultat_3,"► Nombre de km2")
print()


# Requête 4 : Calculer la moyenne d'altitude pour toutes les villes
print("Requête 4 : Altitude de la ville de BORDEAUX")
cursor.execute('''
    SELECT altitude FROM VILLE
    WHERE nom='BORDEAUX'
''')

resultat_4 = cursor.fetchone()
print("Bordeaux est à",resultat_4[0],"mètres d'altitude")
print()


# Requête 5 : Trouver la ville avec l'altitude maximale
cursor.execute('''
    SELECT nom FROM VILLE
    WHERE altitude = (SELECT MAX(altitude) FROM VILLE)
''')
resultat_5 = cursor.fetchone()
print("Requête 5 : Ville avec l'altitude maximale")
print(resultat_5[0])
print()

# Requête 6 : Population totale de la Bretagne
cursor.execute('''
    SELECT nom_region, SUM(population) AS population_totale
    FROM DEPARTEMENT
    WHERE nom_region='Bretagne'
''')

resultat_population_par_region = cursor.fetchall()

# Affichage des résultats
print("Requête 6")
for resultat in resultat_population_par_region:
    population_formatee = '{:,}'.format(resultat[1]).replace(',', '.')  # Utilisation de la fonction format avec remplacement de la virgule par un point
    print(f"Région : {resultat[0]}, Population totale : {population_formatee} habitants")





