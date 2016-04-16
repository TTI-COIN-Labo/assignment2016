#!/bin/sh
<<Usage
USAGE: ./evaluate.sh

This script file should be located in the directry "liblinear-2.1/".
written by JosukeYamane (16, April, 2016)

Usage
cost=10 # a cost value of LIBLINEAR.
./train -c ${cost} -B 1 train_cv0.txt model_c${cost}
./predict test_cv0.txt model_c${cost} out_c${cost} > c_${cost}.log
cat c_${cost}.log
