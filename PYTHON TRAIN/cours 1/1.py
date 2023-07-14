# author smail aghilas 
# test completed with succes let's gooooooooo
def StringChallenge(sen):

    # spité la phrase a des mots
    words = sen.split()
    # définir une variable au en va stocké le mote recent et celui ci en va l'afficher a la fin
    longest_word = ""
    # Une boucle pour parcouir la liste des mots possible
    for word in words:
        # Faire une compaaraison entre le mots actuel et l'anciane mote.
        
        if len(word) > len(longest_word):
            longest_word = word

    # Retourner le mots le plus grande.
    return longest_word