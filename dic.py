import csv
import collections

with open('testttt.csv') as f:
    d = dict(filter(None, csv.reader(f)))

od = sorted(d.items(), key = lambda items:items[1])


with open('sorted.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(od)

