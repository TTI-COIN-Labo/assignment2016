from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaChunkTagger
import sys
tagger = SennaChunkTagger('/usr/share/senna-v2.0')

with open(sys.argv[1], mode='r') as file:
    first_sent = sent_tokenize(file.read().strip())[0]
    word_tag = tagger.tag(word_tokenize(first_sent))
    pre_word = ''
    pre_tag = ''
    for i in range(len(word_tag)):
        word = word_tag[i][0]
        tag = word_tag[i][1]
        if i == 0:
            print(word, end=' ')
            pre_word = word
            pre_tag = tag
            continue
        pre_word = word_tag[i-1][0]
        pre_tag = word_tag[i-1][1]
        if pre_tag == 'O':
            print(pre_tag)
            print(word, end=' ')
        elif tag[:1] == 'I':
            print(word, end=' ')
        elif tag[:1] == 'B':
            print(pre_tag[2:])
            print(word, end=' ')
