"""
freq.py
date: 2016/04/08
author: joe-yama

"""
import sys

word_freq = {}

with open(sys.argv[1], mode='r') as file:
    for line in file:
        words = line.strip().split(" ")
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
for word, freq in sorted(word_freq.items(), key=lambda obj:obj[1], reverse=True):
    print(freq, word)
