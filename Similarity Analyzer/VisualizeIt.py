import scipy
import scipy.spatial
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import pandas as pd
import seaborn as sns

clus20 = pd.read_csv(r"GraphData.csv", sep = ",")
Y20 = scipy.spatial.distance.pdist(clus20[clus20.columns[1:9]], 'cosine')
A = pd.DataFrame(scipy.spatial.distance.squareform(Y20))
mask =  np.tri(A.shape[0], k=-1)
A = np.ma.array(A, mask=mask.T) #Mask upper triangle

sns.set_context({"figure.figsize": (100, 100)})
sns.set_style("white")

fig = plt.figure()
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('hot', 100)
cmap.set_bad('w') # default value is 'k'
ax1.imshow(A, cmap=cmap )
plt.ylabel("Articles", size = 30)
plt.xlabel("Articles", size = 30)
sns.despine()
plt.colorbar(ax1.matshow(A, cmap=cmap, vmin=0, vmax=1), shrink=.75)

ax1.xaxis.set_label_position('bottom')
ax1.xaxis.set_ticks_position('bottom')
plt.xticks(range(1,100,1), size = 3)
plt.yticks(range(1,100,1), size = 3)
plt.show()
#plt.savefig(r'C:\cosine_similarity.jpg', dpi=220, bbox_inches='tight')
