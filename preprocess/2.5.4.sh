#!/bin/sh

head -900 pos_data.txt >> train_cv0.txt
head -900 neg_data.txt >> train_cv0.txt
tail -100 pos_data.txt >> test_cv0.txt
tail -100 neg_data.txt >> test_cv0.txt
wc -l train_cv0.txt
wc -l test_cv0.txt