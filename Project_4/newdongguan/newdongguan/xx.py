#coding=utf-8
import os
from collections import Counter
import jieba

all_words=[]

f = open("spiders/dongguan.json")
content = f.read()
data = jieba.cut(content)
count = Counter(data)
#print count
result = sorted(count.items(),key=lambda x:x[1],reverse=True)
#print result
for word in result:
    print word[0],word[1]
