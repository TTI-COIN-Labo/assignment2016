"""
cat.py
date: 2016/04/08
author: joe-yama

"""
import sys

with open(sys.argv[1], mode='r') as file:
    for line in file:
        print(line, end="")
