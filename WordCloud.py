# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:34:36 2022

@author: datap
"""

import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv


# 958 comments
# with open('datapro.txt','r',encoding='utf-8') as f:
#     data = f.read()

with open('datapro.txt','r') as f:
    data = f.read()

# text pre-processing, extract Chinese only
new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
new_data = " ".join(new_data)

# cut the words
seg_list_exact = jieba.cut(new_data, cut_all=True)

result_list = []
with open('stop_words.txt', encoding='utf-8') as f:
    con = f.readlines()
    stop_words = set()
    for i in con:
        i = i.replace("\n", "")
        stop_words.add(i)

for word in seg_list_exact:
    if word not in stop_words and len(word) > 1:
        result_list.append(word)
print(result_list)

# count the word
word_counts = collections.Counter(result_list)
# top100 high-frequency words
word_counts_top100 = word_counts.most_common(100)

csv_file = open('word.csv','w',encoding='utf-8-sig',newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Word","Count"])
for i in range(0,99):
    # for j in range(0,2):
    #     print(word_counts_top100[i][j])
    csv_writer.writerow([word_counts_top100[i][0],word_counts_top100[i][1]])
    
csv_file.close()

# create the word cloud
my_cloud = WordCloud(
    background_color='white',
    width=900, height=600,
    max_words=100,            
    font_path='simhei.ttf',   
    max_font_size=99,         
    min_font_size=16,         
    random_state=50           
).generate_from_frequencies(word_counts)

# show the image
plt.imshow(my_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
