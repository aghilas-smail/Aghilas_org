# author smail aghilas 
# test completed with succes let's gooooooooo
def StringChallenge(sen):

    words = sen.split()
    
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word