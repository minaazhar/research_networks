#average link

#libraries
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, average
from matplotlib import pyplot as plt

#import data
file = './HumanAgeandFatness.csv'
target = open(file, 'r')
datalist = np.loadtxt(file, skiprows = 1, delimiter=',')
print(datalist)
print('first row')
print(datalist[0,:])

X = datalist
print (X.shape)  # 150 samples with 2 dimensions
#print(X)

# generate the linkage matrix
Z = average(X)
print (Z)
print (Z.shape)
print (Z[0])
#row format [idx1, idx2, dist, sample_count].

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()

