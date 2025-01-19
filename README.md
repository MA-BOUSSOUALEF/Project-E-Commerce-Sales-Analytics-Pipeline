![WhatsApp Image 2025-01-19 à 16 32 09_657c7e94](https://github.com/user-attachments/assets/d758941e-6650-4348-b6fa-c128aa164269)
# E-Commerce Sales Analytics Pipeline

## Description

Ce projet consiste à construire un pipeline ETL (Extract, Transform, Load) pour analyser les tendances des ventes, la performance des produits et le comportement des clients à partir d'un jeu de données e-commerce couvrant la période de 2010 à 2023. Le pipeline ingère des données brutes, les nettoie et les transforme avant de les charger dans une base de données PostgreSQL. Ensuite, diverses analyses et visualisations sont réalisées pour en tirer des insights.

## Objectif du Projet

L'objectif principal est de créer une analyse détaillée des ventes, des produits et du comportement des clients grâce à un pipeline ETL complet. Ce projet vous permet d'apprendre à travailler avec des données réelles, à mettre en place un pipeline ETL, et à effectuer des analyses et visualisations utiles pour une entreprise e-commerce.

## Etapes du Projet

### 1. Extraction des Données (ETL - Extract)
L'étape d'extraction consiste à récupérer les données brutes du fichier source (CSV dans ce cas) et à les charger dans un DataFrame. Cela implique également la validation des types de données (comme `InvoiceNo`, `InvoiceDate`, etc.) pour garantir que les données sont correctement formatées pour les étapes suivantes du processus ETL.

### 2. Transformation des Données (ETL - Transform)
Une fois les données extraites, plusieurs transformations sont effectuées pour les rendre prêtes à l'analyse :
- **Gestion des valeurs manquantes** : Les valeurs manquantes dans des colonnes critiques comme `CustomerID` ou `Description` sont traitées.
- **Création de nouvelles colonnes** : Une nouvelle colonne `TotalPrice` est calculée en multipliant la quantité de produits achetés par leur prix unitaire. 
- **Extraction des éléments temporels** : Des colonnes telles que l'Année, le Mois et le Jour sont extraites de la colonne `InvoiceDate` pour permettre des analyses basées sur le temps.
- **Suppression des anomalies** : Les lignes contenant des valeurs négatives dans les colonnes `Quantity` ou `UnitPrice` sont supprimées, car elles peuvent représenter des retours ou des erreurs.

### 3. Chargement des Données dans PostgreSQL (ETL - Load)
Une fois que les données sont nettoyées et transformées, elles sont chargées dans une base de données PostgreSQL. Cette étape permet de stocker les données de manière organisée dans une structure adaptée pour l'analyse :
- **Table staging** : Contient les données brutes initiales.
- **Table des faits** : Contient les transactions de vente (détails des ventes).
- **Tables de dimensions** : Contiennent des informations supplémentaires sur les produits, les clients, et le temps.

### 4. Modélisation des Données
Une fois les données chargées dans la base de données, elles sont organisées dans un schéma en étoile. Ce schéma facilite l'analyse des données et les agrégations :
- **Table des faits** : Enregistre les transactions de vente avec des détails comme `InvoiceNo`, `StockCode`, `Quantity`, `TotalPrice`, etc.
- **Tables de dimensions** :
  - **Produits** : Contient les informations relatives aux produits vendus (`StockCode`, `Description`).
  - **Clients** : Contient les informations sur les clients (`CustomerID`, `Country`).
  - **Temps** : Contient les informations temporelles (`Year`, `Month`, `Day`).

### 5. Analyse et Visualisation des Données
L'objectif de cette étape est d'extraire des insights utiles à partir des données chargées dans la base. Cela inclut :
- **Analyse des produits les plus performants** : Identifier les produits qui génèrent le plus de revenus ou qui sont les plus populaires.
- **Analyse des ventes par pays** : Examiner la répartition des ventes par pays et identifier les régions les plus rentables.
- **Tendances temporelles des ventes** : Analyser les ventes par période (jour, mois, année) pour détecter les pics ou les périodes creuses.
- **Comportement des clients** : Analyser des métriques comme la dépense moyenne par client, les habitudes d'achat et la fidélité.

Pour cette analyse, des outils comme Python (avec des bibliothèques telles que Matplotlib et Seaborn) ou des outils de visualisation comme Tableau ou Power BI peuvent être utilisés pour créer des graphiques et des rapports interactifs.

## Résultats Attendus

A partir des analyses réalisées, vous pourrez répondre à des questions importantes telles que :
- Quels sont les produits générant le plus de revenus ?
- Quelles sont les périodes de vente les plus intenses ?
- Quels pays ou régions contribuent le plus aux revenus ?
- Quels sont les comportements d'achat typiques des clients ?

## Pourquoi ce Projet est Utile pour les Débutants

Ce projet est une excellente opportunité pour apprendre à travailler avec des données réelles, à comprendre le processus ETL, et à acquérir des compétences en analyse de données. Il vous enseigne comment :
- Charger et nettoyer des données.
- Organiser des données dans une base de données relationnelle.
- Effectuer des analyses approfondies pour en tirer des informations commerciales précieuses.
  
## Prérequis

- Python 3.x
- PostgreSQL (ou un autre SGBD compatible avec SQLAlchemy)
- Bibliothèques Python nécessaires : pandas, SQLAlchemy, matplotlib, seaborn

## Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/votre-utilisateur/ecommerce-sales-analytics-pipeline.git
