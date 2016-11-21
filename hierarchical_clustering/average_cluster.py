#average link

#libraries
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, average
from matplotlib import pyplot as plt
from scipy.spatial import distance

#####################################functions
def condensed_index(n, i, j):
    """
    Calculate the condensed index of element (i, j) in an n x n condensed
    matrix.
    """
    if i < j:
        return n * i - (i * (i + 1) / 2) + (j - i - 1)
    elif i > j:
        return n * j - (j * (j + 1) / 2) + (i - j - 1)

def condensed_distance_matrix(X):
  #make condense distance matrix
  n= len(X)
  distance_vector = np.zeros((n*n-n)/2)
  for i in range(n):
    for j in range(i+1,n):
      distance_vector[condensed_index(n, i, j)]= np.linalg.norm(X[i,:]-X[j,:])
  return distance_vector
  
def average_distance(D,cluster_i,cluster_j,n):
  #calculate average distance, TODO: why this is different than formula
  distance=0
  for i in cluster_i:
    for j in cluster_j:
      distance=distance+D[condensed_index(n, i, j)]
  return distance/(len(cluster_i)*len(cluster_j)) 

######################################code runs heres 
#import data
file = './HumanAgeandFatness.csv'
target = open(file, 'r')
datalist = np.loadtxt(file, skiprows = 1, delimiter=',')
print(datalist)
print('first row')
print(datalist[0,:])

X = datalist
n = len(X)
#create Z matrix with results
Z = np.zeros((n - 1, 4))
#generate distance condense matrix
D = condensed_distance_matrix(X) 
D_original = D #this one is to calculate distances using original distances

#to keep track of members in a cluster
cluster_member = []
cluster_number = []
for i in range(n):
  cluster_member.append([i])
  cluster_number.append(i)
 
##################################Iterations
for k in range(n-1):
  #check for minimun distance
  min_distance = np.amax(D)+1
  for i in range(n):
    for j in range(i+1,n):
      if ((len(cluster_member[i])>0) and (len(cluster_member[j])>0)):
        distance_temp = D[condensed_index(n, i, j)]
        if(distance_temp<min_distance):
          min_distance = distance_temp
          x=i
          y=j
          
  #combine cluster: erase 1st cluster, add 1st cluster to 2nd one
  #save in Z
  nx = cluster_number[x]
  ny = cluster_number[y]
  Z[k, 0] = cluster_number[x] #1st cluster index
  Z[k, 1] = cluster_number[y] #2nd cluster index
  Z[k, 2] = min_distance #distance
  Z[k, 3] = len(cluster_member[y]) + len(cluster_member[x]) #total number of elements

  #erase one cluster and upgrade second one with combined clusters
  nx = len(cluster_member[x])
  ny = len(cluster_member[y])
  cluster_member[y] = cluster_member[y]+ cluster_member[x]
  cluster_member[x] = []
  cluster_number[y] = n+k

  #update distance condensed matrix
  for i in range(n):
    if( (len(cluster_member[i])>0) and (abs(i-y)>0)):
      D[condensed_index(n, i, y)] = (nx/(nx+ny))*(D[condensed_index(n, i, x)])+(ny/(nx+ny))*(D[condensed_index(n, i, y)])
      #average_distance(D_original,cluster_member[i],cluster_member[y],n) 
   
print (Z)   
Z_ref = average(X)
#row format [idx1, idx2, dist, sample_count]. 
print (Z_ref)

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('data index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()


