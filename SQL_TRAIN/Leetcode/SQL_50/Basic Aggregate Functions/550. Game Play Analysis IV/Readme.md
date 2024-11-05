# Intuition


Pour calculer la fraction de joueurs qui se sont connectés à nouveau le jour suivant leur première connexion, vous devez compter le nombre de joueurs dont la date de première connexion est suivie d'une connexion consécutive le jour suivant. Ensuite, vous divisez ce nombre par le nombre total de joueurs distincts.

# Approche

Nous voulons calculer la fraction de joueurs qui se sont connectés à nouveau le jour suivant leur première connexion. Pour ce faire, nous devons compter deux choses : le nombre de joueurs qui se sont connectés pendant des jours consécutifs et le nombre total de joueurs.

Pour compter le nombre de joueurs qui se sont connectés pendant plusieurs jours consécutifs, nous devons trouver la date de première connexion de chaque joueur et vérifier s'il y a une connexion le jour suivant leur première connexion.

Nous utilisons une sous-requête pour calculer le nombre total de joueurs distincts dans la table Activité. Cela nous donne le dénominateur pour calculer la fraction.

Dans la requête principale, nous filtrons les lignes où l'identifiant du joueur et la date de l'événement (après soustraction d'un jour) correspondent à la date de la première connexion du joueur. Cela garantit que nous ne prenons en compte que les joueurs qui se sont connectés pendant des jours consécutifs.
Nous comptons ensuite les identifiants distincts des joueurs dans les lignes filtrées afin d'obtenir le numérateur pour le calcul de la fraction.

Enfin, nous divisons le numérateur par le dénominateur et arrondissons le résultat à deux décimales à l'aide de la fonction ROUND.
