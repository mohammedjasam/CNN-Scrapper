### Scripted by Mohammed Jasam
### mnqnd@mst.edu

###---Sorts the Column in CSV with Article name and Value---###
import os
import csv
filename='Cosine_Similar_Articles.csv'
name='Cosine Similarity with Article #1'

###---This block of code sorts the values in Descending order!---###
with open('mergedfile.csv') as fi, open(filename, "w") as fo:
    data=csv.reader(fi)
    csv_writer = csv.writer(fo)
    csv_writer.writerows(sorted(data, key=lambda x:float(x[0]), reverse=True))


###---Code to append a Header to the result-set!---###
def defineHeader(filename,name):
    with open(filename) as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open(filename,'w') as f:
        w = csv.writer(f)
        w.writerow([name,'Articles'])
        w.writerows(data)
    pickTop(filename)
    return

###---Picks top matching Articles---###
def pickTop(filename):
    with open(filename, 'r') as f,open('Comparision.csv', 'w') as f_out:
         reader = csv.reader(f)
         writer = csv.writer(f_out)
         for i in range (3):
             for row in reader:
                if(i==3):
                    break
                writer.writerow(row)
                i+=1
    swapCols(filename,name)
    return

###---Code to Swap the Columns in the CSV---###
def swapCols(filename, name):
    with open('comparision.csv', 'r') as infile, open('Final Similarity Report.csv', 'a') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ['Articles',name]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)
        os.remove(filename)
    return

defineHeader(filename,name)
