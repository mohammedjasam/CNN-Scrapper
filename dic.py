import csv
import collections

with open('Workbook1.csv') as f:
    d = dict(filter(None, csv.reader(f)))

#outfile = open( 'sorted.csv', 'w')
    
od=sorted(d.items(), int(d.split(maxsplit=1)[0]))

print(od)
