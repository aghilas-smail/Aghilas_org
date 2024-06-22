import re
def SearchingChallenge(strParam):
  # fair une recherche dans la phrase si il existe deja des mots qui ont des numbers
  numbers = re.findall(r'\d+', strParam)
  # faire un petit somme de tout les  nombre vue dans la phrase séléctionnée
  total = sum(int(num) for num in numbers)
    # affichier le code final
  return total
# keep this function call here 
print(SearchingChallenge(input()))

# deuxieme méthode de faire 
'''
def SearchingChallenge(strParam):
  numbers= re.findall(r'\d+', strParam)
  total = 0
  for summ in numbers:
    summ = samm + sum(numbers)
  
  return summ
'''