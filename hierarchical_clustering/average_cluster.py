#average link

#libraries
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, average
from matplotlib import pyplot as plt
from scipy.spatial import distance

def condensed_index(n, i, j):
    """
    Calculate the condensed index of element (i, j) in an n x n condensed
    matrix.
    """
    if i < j:
        return n * i - (i * (i + 1) / 2) + (j - i - 1)
    elif i > j:
        return n * j - (j * (j + 1) / 2) + (i - j - 1)

'''def average_hw(y):
  #number of observations
  n = len(y) 
  #Pairwise distances between observations in n-dimensional space. Returns a condensed distance matrix Y. For each i and j (where i<j<n), the metric dist(u=X[i], v=X[j]) is computed and stored in entry ij.
  #distance = distance.pdist(y) #size 153
  
  #make empty matrix for final output
  Z_arr = np.empty((n - 1, 4))
  
  D = distance.pdist(y)
  print(D)
  chain_length = 0
  size = np.ones(n)
  cluster_chain = np.zeros(n)
  
  #loop for algorithm, n-1
  for k in range(n - 1):
        #initizialization
        if chain_length == 0:
          chain_length = 1
          for i in range(n):
            if size[i] > 0:
              cluster_chain[0] = i
              break
          print ("chain_length")
          print (chain_length)
          print ("size")
          print (size)
          print ("cluster_chain")
          print (cluster_chain)  
        # Go through chain of neighbors until two mutual neighbors are found.
        while True:
            x = cluster_chain[chain_length - 1]

            # We want to prefer the previous element in the chain as the
            # minimum, to avoid potentially going in cycles.

            if chain_length > 1:
                y = cluster_chain[chain_length - 2]
                current_min = D[condensed_index(n, x, y)]
            else:
                current_min = 10e10
            print ("current_min")
            print(current_min,y)
            for i in range(n):
                if size[i] == 0 or x == i:
                    continue

                dist = D[condensed_index(n, x, i)]
                if dist < current_min:
                    current_min = dist
                    y = i

            if chain_length > 1 and y == cluster_chain[chain_length - 2]:
                break

            cluster_chain[chain_length] = y
            chain_length += 1
        #WHILE FINISHED
    
        # Merge clusters x and y and pop them from stack.
        chain_length -= 2

        # This is a convention used in fastcluster.
        if x > y:
            x, y = y, x

        # get the original numbers of points in clusters x and y
        nx = size[x]
        ny = size[y]

        # Record the new node.
        Z[k, 0] = x
        Z[k, 1] = y
        Z[k, 2] = current_min
        Z[k, 3] = nx + ny
        size[x] = 0  # Cluster x will be dropped.
        size[y] = nx + ny  # Cluster y will be replaced with the new cluster

        # Update the distance matrix.
        for i in range(n):
            ni = size[i]
            if ni == 0 or i == y:
                continue

            D[condensed_index(n, i, y)] = new_dist(
                D[condensed_index(n, i, x)],
                D[condensed_index(n, i, y)],
                current_min, nx, ny, ni)

    # Sort Z by cluster distances.
    order = np.argsort(Z_arr[:, 2], kind='mergesort')
    Z_arr = Z_arr[order]

    # Find correct cluster labels inplace.
    label(Z_arr, n)

    return Z_arr
            
  return n'''

 
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
Z = linkage(X)
print (Z)
print (Z.shape)
print (Z[0])
#row format [idx1, idx2, dist, sample_count].

'''plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()'''

#X is data
#D is distance matrix (condense)
#
#Z final matrix

##################################first iteration k=0
k=0
n = len(X)
Z = np.empty((n - 1, 4))
#generate distance matrix
D = distance.pdist(X) 

#to keep track of members in a cluster
cluster_member = []
for i in range(n):
  cluster_member.append([str(i)])
  
#find minimun distance
min_distance = 10e10
for i in range(n):
  for j in range(i+1,n):
    distance_temp = D[condensed_index(n, i, j)]
    if(distance_temp<min_distance):
      min_distance = distance_temp
      x=i
      y=j

#save in Z
Z[k, 0] = x
Z[k, 1] = y
Z[k, 2] = min_distance
Z[k, 3] = len(cluster_member[y]) + len(cluster_member[x])
print(x,y,min_distance)
print(Z)
#erase one cluster and upgrade second one
cluster_member[y] = cluster_member[y]+ cluster_member[x]
cluster_member[x] = []
for i in range(n):
  for j in range(i+1,n):
    distance_temp = D[condensed_index(n, i, j)]
print(cluster_member)
#next iteration, new D, keep track clusters


