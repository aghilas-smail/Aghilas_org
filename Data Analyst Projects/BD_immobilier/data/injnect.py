import psycopg2

conn = psycopg2.connect("dbname=projectdb user=postgres password=Aghilas1999.")
cur = conn.cursor()

tables = {
    # "region": "region.csv",
    # "commune": "commune.csv",
    # "populationn": "populationn.csv",
    #"bien": "bien_corr.csv"
    "vente": "vente_corr.csv"
}

for table, file in tables.items():
    with open(file, 'r') as f:
        cur.copy_expert(f"COPY {table} FROM STDIN WITH (FORMAT csv, HEADER true, DELIMITER ',', ENCODING 'UTF8')", f)
    conn.commit()

cur.close()
conn.close()