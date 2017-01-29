from math import*
from decimal import Decimal

#---Euclidean Distance---#   
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
fi = open("testdata.csv")
with open('EuclideanDistance.txt', 'w') as fo:
    v =[]
    for x, line in enumerate(fi):        
        v.append([int(z) for z in (line.split(',')) if z])
        print(euclidean_distance(v[x-1],v[x]),file=fo)

#---Jaccard Distance---#
def jaccard_similarity(x,y): 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
fi = open("testdata.csv")
with open('JaccardDistance.txt', 'w') as fo:    
    v =[]
    for x, line in enumerate(fi):        
        v.append([int(z) for z in (line.split(',')) if z])
        print(jaccard_similarity(v[x-1],v[x]),file=fo)

#---Cosine Distance---#
def square_rooted(x): 
    return round(sqrt(sum([a*a for a in x])),3)
def cosine_similarity(x,y): 
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
fi = open("testdata.csv")
with open('CosineDistance.txt', 'w') as fo:    
    v =[]
    for x, line in enumerate(fi):        
        v.append([int(z) for z in (line.split(',')) if z])
        print(cosine_similarity(v[x-1],v[x]),file=fo)
