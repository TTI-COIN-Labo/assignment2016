"""
cat_cv000.py
date: 2016/04/08
author: joe-yama

"""

with open("cv000_29590.txt", mode='r') as file:
# ループせず全部いきなり表示してもいいかも
#    for line in file:
#        print(line, end="")
    print file.read()




# あとこれは正直やらなくていいかなって気もしたけど
# ファイル名に神経質なバージョンも考えた！！
import os
import re

filelist = [fname for fname in os.listdir(".") if re.match("cv000.+", fname)]
print filelist

# もうちょい直感的なやつ．でもforループ回さない方法ありそう？
for fname in os.listdir("."):
    if re.match("cv000.+", fname):
        print fname

