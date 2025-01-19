import csv
import psycopg2
from psycopg2.extras import execute_values
import matplotlib.pyplot as plt
from datetime import datetime

# Informations de connexion à PostgreSQL
hostname = '172.25.112.1'
database = 'Ecommerce_db'
username = 'postgres'
pwd = 'Aminereal2002@'
port_id = 5432

# Étape 1 : Extraction des données (CSV)
def load_raw_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                # Convertir les dates au format ISO 8601
                row['InvoiceDate'] = datetime.strptime(row['InvoiceDate'], '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                print(f"Erreur de conversion de date pour la ligne : {row}")
                continue
            row['Quantity'] = int(row['Quantity'])
            row['UnitPrice'] = float(row['UnitPrice'])
            row['TotalPrice'] = row['Quantity'] * row['UnitPrice']  # Calculer TotalPrice
            data.append(row)
    return data

# Étape 2 : Transformation des données
def transform_data(data):
    transformed = []
    for row in data:
        # Supprimer les lignes invalides
        if row['Quantity'] > 0 and row['UnitPrice'] > 0:
            # Remplir les valeurs manquantes
            row['CustomerID'] = int(row['CustomerID']) if row['CustomerID'] else 0
            row['Description'] = row['Description'] or 'Unknown'
            transformed.append(row)
    return transformed

# Étape 3 : Création des tables dans PostgreSQL
def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS staging_sales_data (
                InvoiceNo VARCHAR(20),
                StockCode VARCHAR(20),
                Description TEXT,
                Quantity INT,
                InvoiceDate TIMESTAMP,
                UnitPrice NUMERIC(10, 2),
                CustomerID INT,
                Country VARCHAR(100),
                TotalPrice NUMERIC(10, 2)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS fact_sales (
                TransactionID SERIAL PRIMARY KEY,
                InvoiceNo VARCHAR(20),
                StockCode VARCHAR(20),
                Quantity INT,
                TotalPrice NUMERIC(10, 2),
                InvoiceDate TIMESTAMP,
                CustomerID INT,
                Country VARCHAR(100)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS dim_products (
                StockCode VARCHAR(20) PRIMARY KEY,
                Description TEXT
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS dim_customers (
                CustomerID INT PRIMARY KEY,
                Country VARCHAR(100)
            );
        """)
        conn.commit()
        print("Tables créées avec succès.")

# Étape 4 : Charger les données dans PostgreSQL
def load_data_to_postgres(data, conn, table_name):
    with conn.cursor() as cur:
        keys = data[0].keys()
        columns = ', '.join(keys)
        values = [[row[key] for key in keys] for row in data]
        query = f"INSERT INTO {table_name} ({columns}) VALUES %s"
        execute_values(cur, query, values)
        conn.commit()
        print(f"Données chargées dans la table {table_name}.")

# Étape 5 : Analyse et visualisation
def analyze_data(conn):
  # #les commandes de chaque pays
  #   query = """
  #       SELECT Country, SUM(TotalPrice) AS TotalSales
  #       FROM staging_sales_data
  #       GROUP BY Country
  #       ORDER BY TotalSales DESC;
  #   """
  #   #Top 5 des produits les plus vendus 
  #   query = """
  #       SELECT StockCode, SUM(Quantity) AS TotalQuantity
  #       FROM fact_sales
  #       GROUP BY StockCode
  #       ORDER BY TotalQuantity DESC
  #       LIMIT 5;

  #   """
  #   #Revenus par mois 
  #   query = """
  #       SELECT EXTRACT(MONTH FROM InvoiceDate) AS Month, SUM(TotalPrice) AS Revenue
  #       FROM fact_sales
  #       GROUP BY Month
  #       ORDER BY Month;


  #   """
  #   #Nombre de clients uniques par pays 
  #   query = """
  #       SELECT Country, COUNT(DISTINCT CustomerID) AS UniqueCustomers
  #       FROM fact_sales
  #       GROUP BY Country;
  #   """
  #   with conn.cursor() as cur:
  #       cur.execute(query)
  #       result = cur.fetchall()

  #   # Préparer les données pour la visualisation
  #   countries = [row[0] for row in result]
  #   total_sales = [row[1] for row in result]

  #   # Visualisation
  #   plt.figure(figsize=(10, 5))
  #   plt.bar(countries, total_sales, color='skyblue')
  #   plt.title('Ventes par pays')
  #   plt.xlabel('Pays')
  #   plt.ylabel('Ventes totales')
  #   plt.xticks(rotation=45)
  #   plt.tight_layout()
  #   plt.show()
  # Initialiser les listes de données
      data_queries = [
          {
              "query": """
                  SELECT Country, SUM(TotalPrice) AS TotalSales
                  FROM staging_sales_data
                  GROUP BY Country
                  ORDER BY TotalSales DESC
                  LIMIT 5;
              """,
              "title": "Ventes totales par pays",
              "xlabel": "Pays",
              "ylabel": "Ventes totales",
              "type": "bar",
              "color": "skyblue"
          },
          {
              "query": """
                  SELECT description, SUM(Quantity) AS TotalQuantity
                  FROM staging_sales_data
                  GROUP BY description
                  ORDER BY TotalQuantity DESC
                  LIMIT 5;
              """,
              "title": "Top 5 des produits les plus vendus",
              "xlabel": "Code produit",
              "ylabel": "Quantité totale",
              "type": "bar",
              "color": "green"
          },
          {
              "query": """
                  SELECT EXTRACT(MONTH FROM InvoiceDate) AS Month, SUM(TotalPrice) AS Revenue
                  FROM staging_sales_data
                  GROUP BY Month
                  ORDER BY Month;
              """,
              "title": "Revenus par mois",
              "xlabel": "Mois",
              "ylabel": "Revenus",
              "type": "line",
              "color": "green"
          }, 
          {
              "query": """
                  SELECT Country, COUNT(DISTINCT CustomerID) AS UniqueCustomers
                  FROM staging_sales_data
                  GROUP BY Country
                  ORDER BY Country DESC
                  LIMIT 5;
              """,
              "title": "Nombre de clients uniques par pays",
              "xlabel": "Pays",
              "ylabel": "Clients uniques",
              "type": "bar",
              "color": "red"
          }
      ]

      # Préparer la figure
      fig, axes = plt.subplots(2, 2, figsize=(15, 10))
      axes = axes.flatten()
      fig.patch.set_facecolor('black')

      for i, data_query in enumerate(data_queries):
          with conn.cursor() as cur:
              cur.execute(data_query["query"])
              result = cur.fetchall()

          # Préparer les données pour le graphique
          labels = [row[0] for row in result]
          values = [row[1] for row in result]

          ax = axes[i]
          ax.set_facecolor('black')  # Modifier le fond des axes (graphiques) en noir
          ax.spines['top'].set_color('white')  # Les bordures du graphique en blanc
          ax.spines['right'].set_color('white')
          ax.spines['left'].set_color('white')
          ax.spines['bottom'].set_color('white')

          # Changer la couleur des ticks (étiquettes sur les axes)
          ax.tick_params(axis='x', rotation=45, colors='white')  # Couleur des ticks sur l'axe x
          ax.tick_params(axis='y', colors='white')  # Couleur des ticks sur l'axe y

          # Création des graphiques
          if data_query["type"] == "bar":
              ax.bar(labels, values, color=data_query["color"])
          elif data_query["type"] == "line":
              ax.plot(labels, values, marker='o', linestyle='-', color=data_query["color"])

          # Configurer les graphiques
          ax.set_title(data_query["title"], color='white')  # Titre en blanc
          ax.set_xlabel(data_query["xlabel"], color='white')  # Légende de l'axe x en blanc
          ax.set_ylabel(data_query["ylabel"], color='white')  # Légende de l'axe y en blanc

      # Ajuster la mise en page
      plt.tight_layout()
      plt.show()

    

# Pipeline principal
def main():
    file_path = 'data.csv'
    conn = None

    try:
        # Connexion à la base de données
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        print("Connexion réussie avec psycopg2 !")

        # Charger et transformer les données
        raw_data = load_raw_data(file_path)
        transformed_data = transform_data(raw_data)

        # Créer les tables
        #create_tables(conn)

        # Charger les données dans PostgreSQL
      #load_data_to_postgres(transformed_data, conn, 'staging_sales_data')

        # Analyser et visualiser
        analyze_data(conn)

    except Exception as error:
        print(f"Erreur : {error}")

    finally:
        if conn:
            conn.close()
            print("Connexion fermée.")

if __name__ == "__main__":
    main()
