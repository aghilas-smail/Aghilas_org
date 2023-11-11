import numpy as np

# Création d'un tensor unidimensionnel (un vecteur)
tensor = np.array([1, 2, 3, 4, 5])

# Accéder aux éléments du tensor
print(tensor[0])  # Affiche le premier élément (1)
print(tensor[2])  # Affiche le troisième élément (3)
print(tensor[4])

# Opérations sur le tensor
result = tensor * 2  # Multiplie chaque élément par 2
print(result)  # Affiche [2, 4, 6, 8, 10]
