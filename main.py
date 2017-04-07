import longest
import cosine
import jaccard
import lsa
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:27:55 2016

@author: aditya trilok
"""

import xml.etree.ElementTree as ET
# place the data in the working directory. OR just change the directory
tree = ET.ElementTree(file='C:\\Datascience\manner.xml')
from collections import Counter
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import random
vectorizer = TfidfVectorizer(use_idf=True, ngram_range=(1, 3))
MAX_LIMIT = 8000
#nltk.download()
# method for preprocessing
def pre_process(s):
    if s is None:
        return s

    p = string.punctuation
    s = s.lower()
    s = s.strip()
    d = string.digits
    a = p + d
    b = len(a) * " "
    table = str.maketrans(a, b)
    s = s.translate(table)
    stopwords = nltk.corpus.stopwords.words("english")
    stopwords.append(['how'])
    words = s.split()
    s = [w for w in words if w not in stopwords]
    s = ' '.join(s)
    return s


def get_content():
    ques_list = []
    question = pre_process(elem.findtext("subject"))
    content = pre_process(elem.findtext("content"))
    best = pre_process(elem.findtext("bestanswer"))
    ques_list = [best, question, content]
    for ans in elem.iter('nbestanswers'):
        for answer_item in ans.iter('answer_item'):
            ques_list.append(pre_process(answer_item.text))

    return ques_list

health_data = []
family_data = []
science_data = []
finance_data = []

for elem in tree.iter(tag='document'):
    if (elem.findtext("maincat")) == "Health":
        health_data.append(get_content())

    if (elem.findtext("maincat")) == "Family & Relationships":
        family_data.append(get_content())

    if (elem.findtext("maincat")) == "Science & Mathematics":
        science_data.append(get_content())

    if (elem.findtext("maincat")) == "Business & Finance":
        finance_data.append(get_content())


def accuracy(data):
    a = 0
    b = 0
    c = 0
    for element in data:
        a += cosine.get_similarity(element)
        b += longest.long_ans(element)
        c += jaccard.get_similarity(element)

    return a, b, c

def accu(data):
    lsa1 = 0
    lsa2 = 0
    for element in data:
        a, b = lsa.get_similarity(element)
        lsa1 += a
        lsa2 += b
    return lsa1, (lsa1+lsa2)

def iterate_lsa(all_data):
    if len(all_data) < MAX_LIMIT:
        new_data = all_data
    else:
        new_data = random.sample(all_data, MAX_LIMIT)

    a, b = accu(new_data)
    l = len(new_data)
    print('Accuracy using LSA, selecting 1 best answers  :', (a / l))
    print('Accuracy using LSA, selecting 2 best answers  :', (b / l))

def iterate_data(all_data):
    a, b, c = accuracy(all_data)
    l = len(all_data)
    print('Accuracy for Cosine-Similarity: ', (a / l))
    print('Accuracy for Longest Answer: ', (b / l))
    print('Accuracy for Jaccard-Similarity: ', (c / l))




print('*********************************************************************************************************')
print('Health\n')
iterate_data(health_data)
iterate_lsa(health_data)

print('*********************************************************************************************************')
print('Family & Relationships\n')
iterate_data(family_data)
iterate_lsa(family_data)

print('*********************************************************************************************************')
print('Science & Mathematics\n')
iterate_data(science_data)
iterate_lsa(science_data)

print('*********************************************************************************************************')
print('Business & Finance\n')
iterate_data(finance_data)
iterate_lsa(finance_data)