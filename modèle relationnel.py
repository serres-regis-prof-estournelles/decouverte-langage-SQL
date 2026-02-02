import sqlite3

def afficher_modele_relationnel(base_de_donnees):
    # Connexion à la base de données
    conn = sqlite3.connect(base_de_donnees)
    cursor = conn.cursor()

    # Récupération des tables dans la base de données
    tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = cursor.execute(tables_query).fetchall()

    # Affichage du modèle relationnel pour chaque table
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")

        # Récupération des colonnes de la table
        columns_query = f"PRAGMA table_info({table_name});"
        columns = cursor.execute(columns_query).fetchall()

        # Récupération des clés primaires de la table
        primary_keys_query = f"PRAGMA table_info({table_name});"
        primary_keys = [col[1] for col in cursor.execute(primary_keys_query).fetchall() if col[5] == 1]

        # Récupération des clés étrangères de la table
        foreign_keys_query = f"PRAGMA foreign_key_list({table_name});"
        foreign_keys = cursor.execute(foreign_keys_query).fetchall()

        # Affichage des colonnes, clés primaires et clés étrangères
        for column in columns:
            column_name = column[1]
            data_type = column[2]
            is_primary_key = "PRIMARY KEY" if column_name in primary_keys else ""
            print(f"  {column_name} ({data_type}) {is_primary_key}")

        for foreign_key in foreign_keys:
            foreign_key_table = foreign_key[2]
            foreign_key_column = foreign_key[3]
            print(f"  FOREIGN KEY ({foreign_key_column}) REFERENCES {foreign_key_table}")

        print("\n")

    # Fermeture de la connexion
    conn.close()

# Exemple d'utilisation
nom_base_de_donnees = "villes_en_france.db"
afficher_modele_relationnel(nom_base_de_donnees)


