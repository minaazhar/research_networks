'''
Mina Azhar
dijkstra algorith implementation
Reference: #https://www.youtube.com/watch?v=gdmfOwyQlcI
'''
from collections import defaultdict, deque
import numpy as np
import random
import matplotlib.pyplot as plt
####################################################################PART 1: class and functions
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list) #TODO: why to use defaultdict?
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def getlowestdistancenode(distances,unvisited):
  i=0
  closest_node = ''
  #start getting maximun value of the distances
  #v=max(distances.values())
  lowesdistance =  0
  for key in unvisited:
    #first time when no distance has been recorded
    if ((distances[key]>0) and (lowesdistance==0)):
      lowesdistance = distances[key]
      closest_node = key

    if ((distances[key]>0) and (distances[key]<lowesdistance)):
      lowesdistance = distances[key]
      closest_node = key
  return closest_node

def dijkstra(from_point,distances,graph,path):
  distance_accumulated = distances[from_point]
  path_accumulated = path[from_point]
  for neighborn in graph.edges[from_point]:
    print (neighborn)

    #first check if edge it was writen a,b or b,a, and assign axuliar distance
    key = (neighborn,from_point)
    if key in graph.distances:
      distance_aux = graph.distances[neighborn,from_point]
    else:
      distance_aux= graph.distances[from_point,neighborn]
    #once distance is calculated first check if distance to that node is negative, if its, first time visited , if not visited, check if distance calculated is larger or lower
    if distances[neighborn]<0:
      distances[neighborn] = distance_aux+distance_accumulated
      path[neighborn] = path_accumulated+from_point+','
      #path would be origin
    else:
      #only assing if its lower, otherwise, ignore
      if ((distance_aux+distance_accumulated )<distances[neighborn]):
        distances[neighborn] = distance_aux+distance_accumulated
        path[neighborn] = path_accumulated+from_point+','

  return distances,path
####################################################################PART 2: class and functions
########################################################################code runs
#class definitions
graphaux = Graph()

#create N random points
N=8
np.random.seed(4711) #this is to create repetitive random points for display propose
randPoints = np.random.random((N,2))
i=0
#add nodes
for point in randPoints:
    graphaux.add_node(str(i))
    i=i+1

#assing N/2 origin
originPoints = randPoints[0:N/2,:]

#assign N/2 to destination
destinationPoints = randPoints[N/2:,:]

print(randPoints)
print(originPoints)
print(destinationPoints)

#adding and calculating all edges
i=0
for point_a in originPoints:
    j=int(N/2)
    for point_b in destinationPoints:
        graphaux.add_edge(str(i),str(j),np.linalg.norm(point_a-point_b))
        j=j+1
    i=i+1

#checking results
print ("nodes")
print(graphaux.nodes)
print ("edges")
print(graphaux.edges)
print ("distances")
print(graphaux.distances)

################################################################define initial_node and final_nodel
initial_node = '0'
final_node = '3'
unvisited = set(graphaux.nodes)
visited = set()
distances = {}
path_to_origin = {}

#initialize distances
for node in graphaux.nodes:
  distances[node] =-1

#initialize paths
for node in graphaux.nodes:
  path_to_origin[node] =''
################################################################Initialization
#first visit for start point
distances[initial_node]=0
from_point = initial_node
unvisited.remove(from_point)
visited.add(from_point)
distances,path_to_origin  = dijkstra(from_point,distances,graphaux,path_to_origin)
#############################################################loop until final point is visited
while (final_node in unvisited):
    #from the remaining distances that are not -1, what is min -- the name
    from_point = getlowestdistancenode(distances,unvisited)
    print("from point:")
    print(from_point)
    unvisited.remove(from_point) #the min, we remove it from unvisited
    visited.add(from_point)#the min, we add it from visited

    distances,path_to_origin = dijkstra(from_point,distances,graphaux,path_to_origin)

    print("Updates:")
    print ("distances: ",distances)
    print ("unvisited: ",unvisited)
    print ("visited: ", visited)
    print ("paths: ",path_to_origin)

print("Final path from node"+initial_node +" to node "+ final_node+": "+path_to_origin[final_node]+final_node)

#plot figures of network
#first plot originPoints and then destinationPoints
plt.figure(11)
plt.plot( originPoints[:,0],originPoints[:,1], 's',color='g',markersize=15)
plt.plot( destinationPoints[:,0],destinationPoints[:,1], 'o',color='b',markersize=15)

#second: plot all connections edges
for point_a in originPoints:
    print ((point_a))
    j=int(N/2)
    for point_b in destinationPoints:

        plt.plot( [point_a[0],point_b[0]],[point_a[1],point_b[1]], '-',color='k',markersize=15)
        j=j+1
    i=i+1

#third: plot final path
final_path = path_to_origin[final_node]+final_node
final_path_nodes = final_path .split(",")
#ax = plt.axes()
for i in range(len(final_path_nodes)-1):
    x = [randPoints[int(final_path_nodes[i]),0],randPoints[int(final_path_nodes[i+1]),0]]
    y = [randPoints[int(final_path_nodes[i]),1],randPoints[int(final_path_nodes[i+1]),1]]
    plt.plot( x,y, '--',color='r',linewidth=3.0)
    '''xi = randPoints[int(final_path_nodes[i]),0]
    yi = randPoints[int(final_path_nodes[i]),1]
    xf = randPoints[int(final_path_nodes[i+1]),0]
    yf =  randPoints[int(final_path_nodes[i+1]),1]
    ax.arrow(xi,yi,xf-xi ,yf-yi)#, head_width=0.02, head_length=0.05, fc='k', ec='k')'''

#plot labels: source: http://stackoverflow.com/questions/40021676/pyplot-label-scatter-plot-with-coincident-points-overlapping-annotations
labels = ['node{0}'.format(i) for i in range(N)]
for label, x, y in zip(labels, randPoints[:, 0], randPoints[:, 1]):
    plt.annotate(
        label,
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.show()
