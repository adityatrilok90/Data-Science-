"""
Created on Thu Apr 28 11:27:55 2016

@author: aditya trilok
"""

import xml.etree.ElementTree as ET
import operator
from functools import reduce
import numpy as np
import itertools
from collections import Counter
import string
import nltk


def get_similarity(element):

    if element[2] == None:
        question = element[1]
    else:
        question = (element[1] + element[2])
    jaccardlist = []
    j = [question] + element[3:]
    set_x = set(j)
    for i in range(3,len(element)):
        k = question + element[i]
        set_y = set(k)
        numerator = len(set_x.intersection(set_y)) #length of intersection of x and y
        denominator = float(len(set_x.union(set_y)))
        jaccardlist.append(numerator / denominator)
    m = jaccardlist.index(max(jaccardlist))
    m = m + 3
    if element[0] == element[m]:
        return 1
    else:
        return 0
