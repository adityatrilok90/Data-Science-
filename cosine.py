"""
Created on Thu Apr 28 11:27:55 2016

@author: aditya kashyap
"""

import xml.etree.ElementTree as ET
import operator
from functools import reduce
import numpy as np
import itertools
from collections import Counter
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_similarity_score
vectorizer = TfidfVectorizer(use_idf = True, ngram_range=(1, 3))


def get_similarity(element):
    if element[2] == None:
        ques = element[1]
        question = [element[1]] + element[3:]
    else:
        ques = (element[1] + element[2])
        question = element[1:]
    q= ' '.join(question)
    j = [q]
    for i in range(3, len(element)):
        k = ques + element[i]
        j.append(k)

    similarity = []
    vecter = vectorizer.fit_transform(j)
    A = cosine_similarity(vecter)
    b = A[0]
    similarity = list(b[1:])
    x = max(similarity)
    m = similarity.index(x)
    m = m + 3
    if element[0] == element[m]:
        return 1
    else:
        return 0