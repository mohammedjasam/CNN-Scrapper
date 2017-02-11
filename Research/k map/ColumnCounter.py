import csv

datafilename = 'testdata.csv'
d = ','
f=open(datafilename,'r')

reader=csv.reader(f,delimiter=d)
ncol=len(next(reader)) # Read first line and count columns
f.seek(0)              # go back to beginning of file
for row in reader:
    pass
print(ncol)
