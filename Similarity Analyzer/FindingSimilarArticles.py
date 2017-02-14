### Scripted by Mohammed Jasam
### mnqnd@mst.edu

import csv
import subprocess
import os
import time

###---Regular Expression Removal---###
def regexx(filename):
    inputfile = open(filename, 'r')
    if(filename=="Result_EuclideanDistance.csv"):
        outputfile = open('EuclideanDistance.csv', 'w')
        for line in inputfile:
            line = line.replace('[', '')
            line = line.replace(']', '')
            outputfile.write(line)
        inputfile.close()
        outputfile.close()
    elif(filename=="Result_CosineDistance.csv"):
        outputfile = open('CosineDistance.csv', 'w')
        for line in inputfile:
            line = line.replace('[', '')
            line = line.replace(']', '')
            outputfile.write(line)
        inputfile.close()
        outputfile.close()
    else:
        outputfile = open('JaccardDistance.csv', 'w')
        for line in inputfile:
            line = line.replace('[', '')
            line = line.replace(']', '')
            outputfile.write(line)
        inputfile.close()
        outputfile.close()
    return


###---Write row to col---###
def RowToCol(filename):
    with open(filename, "r") as fi:
        r = csv.reader(fi,delimiter = ',')
        for i in range(0): # count from 0 to n
            next(r)     # and discards the rows
        row = next(r)
        r1 = [float(x) for x in row]
        with open('RowToCol.csv','w') as fo:
            for x in range(100):
                print(r1[x],file=fo)
        mergeCSV('RowToCol.csv')
    return

###---Merge the values with Article Names---###
def mergeCSV(mergefilename):
    with open('artlist.csv', 'r') as book1:
        with open(mergefilename, 'r') as book2:
            reader1 = csv.reader(book1, delimiter=',')
            reader2 = csv.reader(book2, delimiter=',')
            both = []
            for row1, row2 in zip(reader1, reader2):
                row2.append(row1[0])
                both.append(row2)
            with open('mergedfile.csv', 'w') as output:
                writer = csv.writer(output, delimiter=',')
                writer.writerows(both)
    return

#------Finding Similar Articles to Article #1 using all 3 metrices!!-----#

###---Calling the functions!!!---###
def runItAll(filename):
    RowToCol(filename)
    if(filename=="EuclideanDistance.csv"):
        v=" python SortEu.py 1"
    elif(filename=="CosineDistance.csv"):
        v=" python SortCo.py 1"
    else:
        v=" python SortJa.py 1"
    subprocess.call(v, shell=True)
    return


regexx('Result_EuclideanDistance.csv')
runItAll('EuclideanDistance.csv')
regexx('Result_CosineDistance.csv')
runItAll('CosineDistance.csv')
regexx('Result_JaccardDistance.csv')
runItAll('JaccardDistance.csv')
time.sleep(3) #Execution stops for 3 seconds

###---Cleaning the directory---###
os.remove('Comparision.csv')
os.remove('RowToCol.csv')
os.remove('mergedfile.csv')
