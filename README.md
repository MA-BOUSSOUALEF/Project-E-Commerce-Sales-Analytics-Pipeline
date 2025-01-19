# E-Commerce Sales Analytics Pipeline
![WhatsApp Image 2025-01-19 à 16 32 09_657c7e94](https://github.com/user-attachments/assets/d758941e-6650-4348-b6fa-c128aa164269)

# E-Commerce Sales Analytics Pipeline

## Description

Ce projet a pour objectif de créer un pipeline ETL (Extract, Transform, Load) afin d'analyser les tendances de ventes, la performance des produits et le comportement des clients sur un jeu de données e-commerce couvrant la période de 2010 à 2023. En récupérant, nettoyant et transformant les données brutes, ce pipeline les charge ensuite dans une base de données PostgreSQL. À travers différentes analyses, nous explorons des insights utiles pour une meilleure compréhension des ventes et des clients.

## Objectif du Projet

L'objectif est d'analyser un large jeu de données e-commerce pour dégager des tendances et des insights relatifs aux produits, aux ventes et au comportement des clients. Ce projet est une excellente opportunité d'apprendre à traiter des données réelles, à mettre en place un pipeline ETL, et à explorer les données pour en tirer des conclusions pertinentes.

## Étapes du Projet

### 1. Extraction des Données (ETL - Extract)

La première étape consiste à extraire les données depuis un fichier CSV brut. Ces données sont ensuite chargées dans un DataFrame pour pouvoir les traiter. Pendant cette phase, on vérifie que chaque colonne est correctement formatée, comme par exemple la colonne des dates de transaction (`InvoiceDate`) qui doit être convertie au format datetime.

### 2. Transformation des Données (ETL - Transform)

Une fois les données extraites, on passe à la phase de transformation :
- **Gestion des données manquantes** : Parfois, certaines informations sont absentes (par exemple, `CustomerID` ou `Description`). Nous les traitons ou les remplaçons selon les besoins.
- **Création de nouvelles variables** : Par exemple, une colonne `TotalPrice` est calculée en multipliant la quantité de produits achetés par leur prix unitaire.
- **Extraction des informations temporelles** : Pour analyser les tendances de vente dans le temps, nous extrayons l'année, le mois et le jour à partir de la date de la transaction.
- **Suppression des anomalies** : Les valeurs négatives dans des colonnes comme `Quantity` ou `UnitPrice` sont souvent des erreurs ou des retours produits, donc elles sont éliminées pour garantir la qualité des données.

### 3. Chargement des Données dans PostgreSQL (ETL - Load)

Une fois les données nettoyées et transformées, nous les chargeons dans une base de données PostgreSQL. Cela nous permet de stocker les données de manière structurée et prête pour l'analyse :
- Une **table staging** pour stocker les données brutes.
- Une **table des faits** pour enregistrer les transactions, avec des informations détaillées sur chaque vente.
- Des **tables de dimensions** pour les produits, les clients et les informations temporelles.

### 4. Modélisation des Données

Pour faciliter l'analyse, les données sont organisées en un schéma en étoile. Ce modèle comprend :
- **Table des faits** : Où toutes les transactions sont enregistrées, avec des détails comme le numéro de facture, le code produit, la quantité, le prix total, etc.
- **Tables de dimensions** :
  - **Produits** : Informations sur les produits (`StockCode`, `Description`).
  - **Clients** : Données sur les clients (`CustomerID`, `Country`).
  - **Temps** : Informations temporelles permettant d'analyser les ventes par année, mois et jour.

### 5. Analyse et Visualisation des Données

À ce stade, nous utilisons les données chargées pour répondre à des questions clés et générer des insights. Les analyses comprennent :
- **Produits les plus performants** : Identifier les produits qui génèrent le plus de revenus ou qui sont les plus populaires.
- **Ventes par pays** : Analyser la répartition géographique des ventes pour voir quels pays ou régions sont les plus rentables.
- **Tendances temporelles des ventes** : Analyser l’évolution des ventes au fil du temps pour repérer des pics ou des périodes creuses.
- **Comportement des clients** : Comprendre les habitudes d’achat des clients, comme la dépense moyenne par client ou la fréquence des achats.

Pour cette phase, des outils comme Python (avec des bibliothèques telles que Matplotlib ou Seaborn) ou des outils de visualisation comme Tableau/Power BI peuvent être utilisés pour créer des graphiques et des rapports interactifs.

## Insights

Les analyses permettent de répondre à plusieurs questions importantes, telles que :
- Quels sont les produits qui génèrent le plus de revenus ?
- À quels moments de l’année les ventes sont-elles les plus fortes ?
- Quels sont les pays ou régions qui contribuent le plus aux revenus ?
- Quel est le comportement moyen des clients (dépenses, fréquence d’achat, fidélité) ?

## Pourquoi ce Projet est Utile pour les Débutants

Ce projet est idéal pour ceux qui souhaitent se familiariser avec l'analyse de données, car il couvre un processus complet de traitement des données :
- **Extraction et nettoyage des données** : Vous apprendrez à gérer des données brutes et à les transformer pour les rendre prêtes à l’analyse.
- **Stockage des données dans une base de données** : Vous découvrirez comment organiser et stocker des données dans une base relationnelle comme PostgreSQL.
- **Analyse et visualisation des données** : Vous apprendrez à identifier des tendances importantes et à visualiser les résultats pour communiquer des insights pertinents.

## Prérequis

- Python 3.x
- PostgreSQL (ou un autre système de gestion de base de données compatible)
- Bibliothèques Python nécessaires : pandas, SQLAlchemy, matplotlib, seaborn
