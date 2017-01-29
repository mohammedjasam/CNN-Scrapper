import csv
import sys
import os
import csv
import collections
import pandas as pd
from math import*
from decimal import Decimal

def getKey(item):
    return item[0]

with open('final.csv',newline='') as f:
        r = csv.reader(f)
        
        data = [line for line in r]
        next(r)
        #y=data.sort()
        y=sorted(data)
        print(y)
'''



with open('EuclideanDistance.csv') as f:
    d = dict(filter(None, csv.reader(f)))
    next(f)
    od = sorted(d.items(), key = lambda items:items[1])


    with open('sorted.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(od)
'''
