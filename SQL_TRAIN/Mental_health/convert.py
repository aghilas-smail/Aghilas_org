import pandas as pd

# Charger le fichier Excel
file_path = 'Mental_health_Depression_disorder_Data.xlsx'
excel_file = pd.ExcelFile(file_path)

# Afficher les noms des feuilles pour identifier celles que vous voulez extraire
print(excel_file.sheet_names)

# Dictionnaire des tables et des noms de feuilles pour plus de clarté
sheets = {
    'prevalence-by-mental-and-substa': 'prevalence-by-mental-and-substa',
    'depression-by-level-of-educatio': 'depression-by-level-of-educatio',
    'prevalence-of-depression-by-age': 'prevalence-of-depression-by-age',
    'prevalence-of-depression-males-': 'prevalence-of-depression-males-',
    'suicide-rates-vs-prevalence-of-': 'suicide-rates-vs-prevalence-of-',
    'number-with-depression-by-count': 'number-with-depression-by-count'
}

# Lire et enregistrer chaque table dans un fichier Excel séparé
for sheet_name, output_name in sheets.items():
    # Lire la table
    table = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Enregistrer la table dans un nouveau fichier Excel
    output_file = f'{output_name}.xlsx'
    with pd.ExcelWriter(output_file) as writer:
        table.to_excel(writer, sheet_name=sheet_name, index=False)
        
    print(f'Table "{sheet_name}" saved to "{output_file}"')
