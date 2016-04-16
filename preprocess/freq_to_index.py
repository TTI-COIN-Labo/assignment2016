from nltk import tokenize
import sys
id_freq = {}
word_id = {}
with open(sys.argv[1], mode='r') as file:
    sents = tokenize.sent_tokenize(file.read().strip())
    for s in sents:
        for word in tokenize.word_tokenize(s):
            if word in word_id:
                id_freq[word_id[word]] += 1
            else:
                id = len(word_id) + 1
                word_id[word] = id
                id_freq[id] = 1

for id, freq in sorted(id_freq.items(), key=lambda obj:obj[1], reverse=True):
    print(freq, id)
