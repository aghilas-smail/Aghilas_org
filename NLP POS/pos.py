import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Je suis smail aghilas, est ce que ca marche bien ou pas")

for token in doc:
    print(token,"|", token.pos)
    