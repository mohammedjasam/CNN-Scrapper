''' Author - Mohammed Jasam '''

import csv
import sys
import os
import csv
import collections
import pandas as pd
from math import*
from decimal import Decimal


'''
#---Code to do all the formatting---#
def runItAll(mergefilename,name,filename):
    mergeCSV(mergefilename)
    defineHeader(name)
    swapCols(filename,name)
    return


#---Cleans the Repository and Leaves necessary Data and Files---#
def endItAll():
    os.remove('eudist.csv')
    os.remove('jacdist.csv')
    os.remove('cosdist.csv')
    os.remove('final.csv')
    os.remove('sorted.csv')


#---Code to append a Header to the result-set!---#
def defineHeader(name):
    with open('sorted.csv',newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open('sorted.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow([name,'Articles'])
        w.writerows(data)
    return


#---Code to merge both CSV Files---#
def mergeCSV(mergefilename):
    with open('artlist.csv', 'r') as book1:
        with open(mergefilename, 'r') as book2:
            reader1 = csv.reader(book1, delimiter=',')
            reader2 = csv.reader(book2, delimiter=',')
            both = []
            for row1, row2 in zip(reader1, reader2):
                row2.append(row1[0])
                both.append(row2)
            with open('final.csv', 'w') as output:
                writer = csv.writer(output, delimiter=',')
                writer.writerows(both)
    sortResult('final.csv')
    return


#---Code to Swap the Columns in the CSV---#
def swapCols(filename, name):
    with open('sorted.csv', 'r') as infile, open(filename, 'a') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ['Articles',name]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)
    return


#---Code to Sort the Result-Set---#
def sortResult(filename):
    with open(filename) as f:
        d = dict(filter(None, csv.reader(f)))

    od = sorted(d.items(), key = lambda items:items[0])


    with open('sorted.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(od)
    return

'''
#---Euclidean Distance---#
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
fi = open("testdata.csv")
row_count = sum(1 for row in fi)
print(row_count)
with open('eudist.csv', 'w') as fo:
    v =[]
    for count in range(row_count):
        #print(count)
        fi = open("testdata.csv")
        dist = []
        #print (fi)
        #print ("count =" +str(count) )
        for x, line in enumerate(fi):
            article_base = [count]
            article_matching = [x]
            if (count < row_count):
                v.append([int(z) for z in (line.split(',')) if z])
                dist.append(euclidean_distance(v[count],v[x]))
        print (dist, file=fo)
#runItAll('eudist.csv','Euclidean Distance','EuclideanDistance.csv')


#---Jaccard Distance---#
def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
fi = open("testdata.csv")
row_count = sum(1 for row in fi)
print(row_count)
with open('jacdist.csv', 'w') as fo:
    v =[]
    for count in range(row_count):
        fi = open("testdata.csv")
        dist = []
        for x, line in enumerate(fi):
            article_base = [count]
            article_matching = [x]
            if (count < row_count):
                v.append([int(z) for z in (line.split(',')) if z])
                dist.append(jaccard_similarity(v[count],v[x]))
        print (dist, file=fo)
#runItAll('jacdist.csv','Jaccard Distance','JaccardDistance.csv')


#---Cosine Distance---#
def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)
def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
fi = open("testdata.csv")
row_count = sum(1 for row in fi)
print(row_count)
with open('cosdist.csv', 'w') as fo:
    v =[]
    for count in range(row_count):
        fi = open("testdata.csv")
        dist = []
        for x, line in enumerate(fi):
            article_base = [count]
            article_matching = [x]
            if (count < row_count):
                v.append([int(z) for z in (line.split(',')) if z])
                dist.append(cosine_similarity(v[count],v[x]))
runItAll('cosdist.csv','Cosine Distance','CosineDistance.csv')

###----###----###---Let's free the Memory---###----###----###
endItAll()
