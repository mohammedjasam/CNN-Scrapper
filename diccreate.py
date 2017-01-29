import csv
with open('testdata.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = dict(row[:2] for row in reader if row)
print(mydict)
