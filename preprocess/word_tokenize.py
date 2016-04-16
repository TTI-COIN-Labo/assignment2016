from nltk import tokenize
import sys
with open(sys.argv[1], mode='r') as file:
    sents = tokenize.sent_tokenize(file.read().strip())
    for s in sents:
        for word in tokenize.word_tokenize(s):
            print(word)
