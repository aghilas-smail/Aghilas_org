#!/usr/bin/python
import socket

# Créer un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect(('rtd.hpwren.ucsd.edu', 12020))

# Boucle pour recevoir des données
for i in range(0, 60):
    data = s.recv(1024)
    # Décoder les données binaires en chaîne de caractères
    data_str = data.decode('utf-8')
    parts = data_str.split('\t', 2)
    if len(parts) > 2:
        print("{0}: {1}".format(i, parts[2]))

# Fermer le socket
s.close()
