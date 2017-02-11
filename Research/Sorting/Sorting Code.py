import csv
import collections
from collections import OrderedDict

with open('Workbook1.csv') as f:
    d = dict(filter(None, csv.reader(f)))    
    int_docs_info = {int(k) : v for k, v in d.items()}

    for key, value in sorted(int_docs_info.items()): # Note the () after items!
        print(key, value)
#outfile = open( 'sorted.csv', 'w')

'''
SortInputfile=open("Workbook1.csv","r")
line=SortInputfile.readlines()
line.sort(key=lambda line: int(line.split()[1]))
map(SortOutputfile.write, line)
od = sorted(d.items(), key = lambda l: int(l.split(maxsplit=1)[0]))

print(od)

with open('sorted.csv', 'w') as outfile, open('Workbook1.csv') as infile:
    outfile.writelines(sorted(infile,
        key = lambda l: int(l.split(maxsplit=1)[0])))


od = sorted(d, key=d.get,reverse=True)

for r in od:
    print(r, d[r])
'''
