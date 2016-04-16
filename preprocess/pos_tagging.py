from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaTagger
import sys
tagger = SennaTagger('/usr/share/senna-v2.0')
with open(sys.argv[1], mode='r') as file:
    first_sent = sent_tokenize(file.read().strip())[0]
    word_pos = tagger.tag(word_tokenize(first_sent))
    for word, pos in word_pos:
        print(word, pos)
