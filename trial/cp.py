"""
cp.py
date: 2016/04/08
author: joe-yama

"""
import sys
with open(sys.argv[2], mode='a') as dest_file:
    with open(sys.argv[1], mode='r') as source_file:
        for line in source_file:
            dest_file.write(line)
        
    

