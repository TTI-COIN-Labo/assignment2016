from nltk.tokenize import sent_tokenize, word_tokenize
import os
import shelve
import sys
f_list = os.listdir(sys.argv[1])
word_to_id = shelve.open(sys.argv[3])
for f in f_list:
    id_to_freq = {}
    for s in sent_tokenize(open(sys.argv[1] + f, mode='r').read()):
        for w in word_tokenize(s.strip()):
            if not w in word_to_id:
                word_to_id[w] = len(word_to_id) + 1
            id = word_to_id[w]
            if id in id_to_freq:
                id_to_freq[id] += 1
            else:
                id_to_freq[id] = 1
    print(sys.argv[2], end=' ') # print label
    for id, freq in sorted(id_to_freq.items(), key=lambda obj:obj[0]):
        print(str(id)+':'+str(freq), end=' ')
    print()
