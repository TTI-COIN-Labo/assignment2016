from nltk.tokenize import sent_tokenize
import sys
with open(sys.argv[1], mode='r') as file:
    for sent in sent_tokenize(file.read().strip()):
        print(sent)
