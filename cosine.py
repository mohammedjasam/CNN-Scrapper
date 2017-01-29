
from math import*

import csv 
import sys #used for passing in the argument


        

def square_rooted(x):
 
    return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
 
   numerator = sum(a*b for a,b in zip(x,y))
   denominator = square_rooted(x)*square_rooted(y)
   return round(numerator/float(denominator),3)




fi = open("testdata.csv")
v =[]
for x, line in enumerate(fi):
    v.append([int(z) for z in (line.split(',')) if z])
    print(cosine_similarity(v[x-1],v[x]))#,file=fo)
    #print(v[x])

#print(v[2])




































'''
[0.77, 0.34, 0.12, 0.0, 0.0, 0.0]
'''

#x = ["0", "1", "2"]
#y = str(''.join(data))# converting list into string
#z = int(data)

#print(z)


'''
y=str(data[0])
print(y)
z=int(y)
print(z[0])'''
'''for i in range(1):
    print(cosine_similarity(int(str(data[0])),int(str(data[1]))))#,file=fo)
    print(data[0])
   ''' 
