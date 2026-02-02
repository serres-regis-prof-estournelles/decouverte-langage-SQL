import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('villes_en_france.db')
cursor = conn.cursor()

# Requête : Sélectionner toutes les villes d'un département spécifique
num_dep_specifique = '40'
cursor.execute(f'''
    SELECT nom FROM VILLE
    WHERE num_dep = '{num_dep_specifique}'
    ORDER BY nom
''')

# Récupération des résultats
resultats = cursor.fetchall()

# Affichage des résultats sans apostrophes
print(f"Villes du département {num_dep_specifique} :")
for resultat in resultats:
    nom_ville_sans_apostrophe = resultat[0].replace("'", "")
    print(nom_ville_sans_apostrophe)

# Fermer la connexion
conn.close()
