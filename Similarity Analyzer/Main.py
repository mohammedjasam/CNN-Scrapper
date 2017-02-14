### Scripted by Mohammed Jasam
### mnqnd@mst.edu

import csv
import sys
import os
import csv
import collections
import pandas as pd
from math import*
from decimal import Decimal
import time
import subprocess
from multiprocessing import Process
import scipy
import scipy.spatial
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import seaborn as sns
import pandas
import datetime
from pylab import *



###---Creates a DataSet to execute the Algorithms---###
subprocess.call(" python testDataGenerator.py 1", shell=True)
time.sleep(5) # Delay for 5 seconds

###---Visualizes the computational result of the Similarity Algorithms---###
def viz(filename):

    data = pandas.read_csv(filename,  sep = ',')

    timesIndex = data.index

    dynamapsIndex = data.columns

    levels = map(lambda x : round(x,10), linspace(data.min().min(), data.max().max(), 101))

    contourf(data, levels = levels, cmap=plt.cm.jet_r, interpolation = 'bicubic')
    colorbar()
    xticks(range(0, len(dynamapsIndex),5), dynamapsIndex[::5], rotation = 'vertical')
    yticks(range(0, len(timesIndex), 5), timesIndex[::5])
    show()
    return


###---Using Parallel Processing to run the Algorithms simultaneously!!!---###

#---Function to calculate Euclidean Distance---#
def func1():
  def euclidean_distance(x,y):
      return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
  fi = open("testdata.csv")
  row_count = sum(1 for row in fi)
  #print(row_count)
  with open('Result_EuclideanDistance.csv', 'w') as fo:
      v =[]
      for count in range(row_count):
          fi = open("testdata.csv")
          dist = []
          for x, line in enumerate(fi):
              article_base = [count]
              article_matching = [x]
              if (count < row_count):
                  v.append([int(z) for z in (line.split(',')) if z])
                  dist.append(euclidean_distance(v[count],v[x]))
          print (dist, file=fo)
  print('Finished Calculating Euclidean Distance')

#---Function to calculate Jaccard Distance---#
def func2():
  def jaccard_similarity(x,y):
      intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
      union_cardinality = len(set.union(*[set(x), set(y)]))
      return intersection_cardinality/float(union_cardinality)
  fi = open("testdata.csv")
  row_count = sum(1 for row in fi)
  #print(row_count)
  with open('Result_JaccardDistance.csv', 'w') as fo:
      v =[]
      for count in range(row_count):
          fi = open("testdata.csv")
          dist = []
          for x, line in enumerate(fi):
              article_base = [count]
              article_matching = [x]
              if (count < row_count):
                  v.append([int(z) for z in (line.split(',')) if z])
                  dist.append(jaccard_similarity(v[count],v[x]))
          print (dist, file=fo)
  print ('Finished Calculating Jaccard Distance')

#---Function to calculate Cosine Distance---#
def func3():
  def square_rooted(x):
      return round(sqrt(sum([a*a for a in x])),3)
  def cosine_similarity(x,y):
      numerator = sum(a*b for a,b in zip(x,y))
      denominator = square_rooted(x)*square_rooted(y)
      return round(numerator/float(denominator),3)
  fi = open("testdata.csv")
  row_count = sum(1 for row in fi)
  #print(row_count)
  with open('Result_CosineDistance.csv', 'w') as fo:
      v =[]
      for count in range(row_count):
          fi = open("testdata.csv")
          dist = []
          for x, line in enumerate(fi):
              article_base = [count]
              article_matching = [x]
              if (count < row_count):
                  v.append([int(z) for z in (line.split(',')) if z])
                  dist.append(cosine_similarity(v[count],v[x]))
          print(dist,file=fo)
  print ('Finished Calculating Cosine Distance')

###---Main Function---###
if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p3 = Process(target=func3)
  p3.start()
  p1.join()
  p2.join()
  p2.join()

  os.remove('testdata.csv')
  subprocess.call(' python3 FindingSimilarArticles.py 1', shell=True)
  print('')
  ###---Visualizing---###
  print('Visualizing Cosine Similarity Values')
  viz('CosineDistance.csv')
  print('Visualizing Euclidean Similarity Values')
  viz('EuclideanDistance.csv')
  print('Visualizing Jaccard Similarity Values')
  viz('JaccardDistance.csv')
  print('')
  print('Open "Final Similarity Report" for the comparision')
  subprocess.call(' python ranking.py 1', shell=True)
  ###---Cleaning the directory---###
  os.remove('Result_EuclideanDistance.csv')
  os.remove('Result_CosineDistance.csv')
  os.remove('Result_JaccardDistance.csv')
