"""
tr_word.py
date: 2016/04/08
author: joe-yama

"""
import sys

with open(sys.argv[1], mode='r') as file:
    for line in file:
        words = line.strip().split(" ")
        for word in words:
            print(word)
