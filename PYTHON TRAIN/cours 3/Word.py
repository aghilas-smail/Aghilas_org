'''
Je voudrais que vous m'écriviez un simple moteur de vérification orthographique. 
Le langage de requête est un langage très simple de type expression régulière, 
avec un caractère spécial : . (le caractère point), qui signifie EXACTEMENT UN caractère 
(il peut s'agir de n'importe quel caractère). Ainsi, par exemple, "c.t" correspondrait à "cat", 
car le point correspond à n'importe quel caractère. La requête peut contenir un nombre quelconque
de caractères point (ou aucun). Votre correcteur orthographique devra être optimisé pour la vitesse, 
vous devrez donc l'écrire de la manière requise. Il y aura une fonction unique setUp() qui
effectuera tous les prétraitements nécessaires, puis une fonction isMatch() qui devra s'exécuter
aussi vite que possible, en utilisant ces prétraitements. Voici quelques exemples, n'hésitez pas
à demander des précisions. Liste de mots : [cat, bat, rat, drat, dart, drab] Requêtes :
cat -> true c.t -> true .at -> true ..t -> true d..t -> true dr... -> true ... -> vrai .... -> vrai ..... -> false h.t -> false c. -> false */ 
// écrire une fonction // Struct setup(List<String> list_of_words) //
Faites le traitement que vous voulez ici // avec une efficacité raisonnable. 
// Retournez les structures de données que vous souhaitez. // Cette fonction
ne sera exécutée qu'une seule fois // écrire une fonction // bool isMatch(Struct struct, String query)
// Retourne si la requête est une correspondance dans le // dictionnaire (True/False) // 
Doit être optimisé pour la vitesse

Traduit avec DeepL.com (version gratuite)
'''


def setUp(word, input_list):
    word = word.strip()
    temp_list = []
    Ismatch = False
    
    # Test if the word is mutch with the input list.
    if word in input_list:
        Ismatch = True
    elif word is None or len(word) == 0:
        Ismatch = False
    else:
        for w in input_list:
            if len(w) == len(word):
                temp_list.append(w)
        
        for j in range(len(temp_list)):
            count = 0
            for i in range(len(word)):
                if word[i] == temp_list[j][i] or word[i] == '.':
                    count += 1
                else:
                    break
            if count == len(word):
                Ismatch = True
                
    print(Ismatch)

def isMatch(word, input_list):
    return setUp(word, input_list)

isMatch('c.t', ['cat', 'bte', 'art', 'drat', 'dart', 'drab','drabn'])


def setUp(word, list) : 
    word = word.split()
    testliste = []
    isMatch = False
    
    #Test if the world is mutch withe the input liste 
    
    if word in list:
        isMatch = True
    elif word is None or len(word) == 0:
        isMatch = False
    else:
        for w in list:
            if len(w) == len(word):
                testliste.append(w)
                