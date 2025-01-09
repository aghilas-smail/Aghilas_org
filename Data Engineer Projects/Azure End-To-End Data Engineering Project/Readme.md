# Azure End-To-End Data Engineering Project

## Partie Base de donnée:

Créer un compte Azure : Commencez par créer un compte Azure gratuit sur le site suivant : Azure Portal.

Installer SQL Server Management Studio (SSMS) : Téléchargez et installez SQL Server Management Studio (SSMS) de Microsoft. Une fois l'installation terminée, nous utiliserons une base de données existante pour notre travail.

Télécharger une base de données existante : Vous pouvez télécharger un exemple de base de données, microsoft propose des exemplaires de bases de données , depuis ce lien : https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms

Importer la base de données dans SSMS : Après avoir téléchargé la base de données de votre choix, importez-la dans SSMS pour qu'elle soit visible et exploitable dans le logiciel.

## Partie Création des ressources necessaires :

- Crée un resource groupe qui va contenaire tous nous ressources pour réaliser ce projet.
- Commencent par le Data factory.
- Ensuit le data lake Gen2.
- Aprés il faut crée une ressource pour databricks.
- Et enfin crée une ressource pour Synapse.

## Liée Data factory avec la base de données:

- Crée une key dans SSMS avec cette commande :
  create login luke with password = '123456789'
  create user luke for login luke
- Ensuite crée un "control access" dans le panelle a droite.
- Une fois crée, maintenant on crée une certificate dans le pannel de key vault.

## Query pour interagire avec la DB:

<!-- SELECT 
s.name AS SchemaName, 
t.Name AS TableName
FROM sys.tables t
INNER JOIN sys.schemas s
ON t.schema_id = s.schema_id
WHERE s.name = 'SalesLT' -->

## Migration des données.

- Les données sont bien copée de SQL server vers azure data lake notamment le contenaire bronze.
- Maintenant la prochaine étape ca sera d'utiliser databricks pour faire des transformation.

## Partie Databricks.

- Utiliser un ETL pour extract, transform et load les données.
- Utilisation de Data Factory pour faire cela.

### Partie connection entre databrics et data lake:

### Partie contenaire bronze au contenaire silver:

![Description de l'image][def]


### Partie contenaire silve au gold:

[def]: Images/bronze_to_silver.png
