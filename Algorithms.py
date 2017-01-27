from math import*
from decimal import Decimal

#---Euclidean Distance---#   
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
fi = open("input.csv")
with open('EuclideanDistance.txt', 'w') as fo:
    for x, line in enumerate(fi):
        print(euclidean_distance([int(line[x])],[int(line[x+1])]),file=fo)


#---Jaccard Distance---#
def jaccard_similarity(x,y): 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
fi = open("input.csv")
with open('JaccardDistance.txt', 'w') as fo:
    for x, line in enumerate(fi):
        print(jaccard_similarity([int(line[x])],[int(line[x+1])]),file=fo)


#---Cosine Distance---#
def square_rooted(x): 
    return round(sqrt(sum([a*a for a in x])),3)
def cosine_similarity(x,y): 
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
fi = open("input.csv")
with open('CosineDistance.txt', 'w') as fo:
    for x, line in enumerate(fi):
        print(cosine_similarity([int(line[x])],[int(line[x+1])]),file=fo)
        
