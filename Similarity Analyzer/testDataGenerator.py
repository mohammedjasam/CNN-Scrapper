### Scripted by Mohammed Jasam
### mnqnd@mst.edu

import csv

###---Generates the testdata to run the similarity Algorithms!!!---###
with open("Data.csv", "rb") as fp_in, open("testdata.csv", "wb") as fp_out:
    reader = csv.reader(fp_in, delimiter=",")
    header = next(reader)
    writer = csv.writer(fp_out, delimiter=",")
    for row in reader:
        del row[0:2]
        writer.writerow(row)
