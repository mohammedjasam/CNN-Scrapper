import pandas
import datetime
from pylab import *

data = pandas.read_csv('a1.csv',  sep = ',')
# print(data)
# print(data)

timesIndex = data.index
# print(timesIndex)
dynamapsIndex = data.columns

# print(dynamapsIndex[::])
levels = map(lambda x : round(x,10), linspace(data.min().min(), data.max().max(), 101))

contourf(data, levels = levels, cmap=plt.cm.jet_r, interpolation = 'bicubic')
colorbar()
xticks(range(0, len(dynamapsIndex),5), dynamapsIndex[::5], rotation = 'vertical')
yticks(range(0, len(timesIndex), 5), timesIndex[::5])
show()
