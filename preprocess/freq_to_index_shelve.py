from nltk.tokenize import sent_tokenize, word_tokenize
import shelve
import sys
word_to_id = shelve.open(sys.argv[2])
for s in sent_tokenize(open(sys.argv[1], mode='r').read()):
    for w in word_tokenize(s.strip()):
        if w in word_to_id: continue
        word_to_id[w] = len(word_to_id) + 1

