#!/usr/bin/python
import socket
import csv
# Créer un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect(('rtd.hpwren.ucsd.edu', 12020))

with open('fichier.txt', mode='w') as file:
    # Boucle pour recevoir des données
    for i in range(0, 60):
        data = s.recv(1024)
        # Décoder les données binaires en chaîne de caractères
        data_str = data.decode('utf-8')
        file.write(data_str)

# Fermer le socket
s.close()
