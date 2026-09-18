from chunking import sentence_chunking

text = "Atraves da mão divina amor, naveguei, e novos povos encontrei, por tempestades e lendas eu passei."
doc = sentence_chunking(text=text)
for sent in doc:
    print(sent)