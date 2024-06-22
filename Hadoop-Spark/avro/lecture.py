import avro.io
import avro.datafile

# Lecture du fichier Avro et affichage des données
with avro.datafile.DataFileReader(open("users.avro", "rb"), avro.io.DatumReader()) as reader:
    for user in reader:
        print(user)
