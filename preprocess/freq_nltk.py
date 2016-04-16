from nltk import tokenize
import sys
word_freq = {}
with open(sys.argv[1], mode='r') as file:
    sents = tokenize.sent_tokenize(file.read().strip())
    for s in sents:
        for word in tokenize.word_tokenize(s):
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
for word, freq in sorted(word_freq.items(), key=lambda obj:obj[1], reverse=True):
    print(freq, word)
