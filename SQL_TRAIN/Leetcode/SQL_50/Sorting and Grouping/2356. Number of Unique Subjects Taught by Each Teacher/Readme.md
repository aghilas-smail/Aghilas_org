## Intuition

Pour calculer le nombre de matières unique enseignée par chaque enseignant, on va calculer le nombre de matière distinct pour chaque enseignat avec la commande  `COUNT()` et `DISTINCT()`


## Approche

- `COUNT(DISTINCT subject_id)` :  Compte le nombre de matières uniques enseignées par chaque enseignant.
- `GROUP BY` teacher_id : Regroupe les données par teacher_id pour calculer le nombre de matières uniques pour chaque enseignant.
- `ORDER BY` teacher_id : Trie les résultats par techer_id pour une présentation plus claire.
