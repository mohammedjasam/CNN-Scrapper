import numpy as np
e = np.genfromtxt ('Result_EuclideanDistance.csv', delimiter=",")
co = np.genfromtxt ('Result_CosineDistance.csv', delimiter=",")
j = np.genfromtxt ('Result_JaccardDistance.csv', delimiter=",")
# print(len(m))
l=[]

for r in range(len(e)):
    for c in range(r):
        l.append((co[r][c],j[r][c],e[r][c],r+1,c+1))
#
l.sort()
with  open('Combined_Resultant_Pairs.csv','w') as fo:

    for x in range(100):
        print(','.join([str(x) for x in l[x]]), file=fo)
        # print(l[x], file=fo)
