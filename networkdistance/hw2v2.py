#https://www.youtube.com/watch?v=gdmfOwyQlcI

from collections import defaultdict, deque
from heapq import *
import numpy as np
import random
import operator

class Graph(object):
    def __init__(self): #self as argument in all function of class
        self.nodes = set() #define unordered array of nodes -- it store name for the node
        self.edges = defaultdict(list) #initialize dictionary as list without key, no key errors -- 
        self.distances = {} #dictionary
        #self allows us to call it, without it, itll just be a variable in the function

    def add_node(self, value):
        self.nodes.add(value) #adds to the set

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node) #saves to_node as a node connected tof from_node
        self.edges[to_node].append(from_node) #vice versa
        self.distances[(from_node, to_node)] = distance #distance, the key is (from_node, to_node), bad thing is it doesnt recognize opposite way

########################################################################code runs
#class definitions
graphaux = Graph() 
    
#create N random points
N=4
randPoints = np.random.random((N,2)) #N number of rows, 2 number of column
i=0
#add nodes
for point in randPoints: #point will take store a value of in randPoints
    graphaux.add_node(str(i)) #adding the name for each point in a set
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

def getlowestdistancenode(distances,unvisited):
  i=0
  closest_node = ''
  #start getting maximun value of the distances
  #v=max(distances.values())
  lowesdistance =  0
  for key in unvisited:
    #first one when not distance has been recorded
    if ((distances[key]>0) and (lowesdistance==0)):
      lowesdistance = distances[key]
      closest_node = key  
  
    if ((distances[key]>0) and (distances[key]<lowesdistance)):
      lowesdistance = distances[key]
      closest_node = key
  return closest_node   
    
initail_nodel = '0'
unvisited = set(graphaux.nodes) #all nodes in unvisited set
visited = set()
distances = {}

#initialize distances
for node in graphaux.nodes: #nodes is already a string, so we dont need to make it a string again
  distances[node] =-1 #assigning -1 to every node
  
#first visit
distances[initail_nodel]=0

################################################################check first distances to initial neighborns
from_point = initail_nodel
print("from point:")
print(from_point)
unvisited.remove(from_point)
visited.add(from_point)
distance_accumulated = distances[from_point] 
for neighborn in graphaux.edges[from_point]:#calling all neighbors ---loop!! -- closes loop with identation
  print (neighborn)
  
  #first check if edge it was writen a,b or b,a, and assign axuliar distance
  key = (neighborn,from_point)
  if key in graphaux.distances: #cus it can be written the other way around, we check first if its available in that way and save it as distance_aux, if not then we make the oppposite version the distance
    distance_aux = graphaux.distances[neighborn,from_point]
  else:
    distance_aux= graphaux.distances[from_point,neighborn] #just to call out the value
  #once distance is calculated first check if distance to that node is negative, if its, first time visited , if not visited, check if distance calculated is larger or lower
  if distances[neighborn]<0:
    distances[neighborn] = distance_aux+distance_accumulated #if its -1 then you assign the distance + accumulated
  else:
    #only assing if its lower, otherwise, ignore
    if ((distance_aux+distance_accumulated )<distances[neighborn]):
      distances[neighborn] = distance_aux+distance_accumulated

print("final print:")
 
print (distances)
print (unvisited)
print (visited)      
#############################################################next visiting round 
from_point = getlowestdistancenode(distances,unvisited) #from the remaining distances that are not -1, what is min -- the name
print("from point:")
print(from_point)
unvisited.remove(from_point) #the min, we remove it from unvisited
visited.add(from_point)
distance_accumulated = distances[from_point] #we get the name 
for neighborn in graphaux.edges[from_point]:
  print (neighborn)
  
  #first check if edge it was writen a,b or b,a, and assign axuliar distance
  key = (neighborn,from_point)
  if key in graphaux.distances:
    distance_aux = graphaux.distances[neighborn,from_point]
  else:
    distance_aux= graphaux.distances[from_point,neighborn]
  #once distance is calculated first check if distance to that node is negative, if its, first time visited , if not visited, check if distance calculated is larger or lower
  if distances[neighborn]<0:
    distances[neighborn] = distance_aux+distance_accumulated    
  else:
    #only assing if its lower, otherwise, ignore
    if ((distance_aux+distance_accumulated )<distances[neighborn]): #8+3 < 7 -- checking E as a neighbor of C
      distances[neighborn] = distance_aux+distance_accumulated #if it is smaller then we reassign
    #if its not smaller then we dont do anything which is shown by nothing written (cus theres no else)
print("final print:")
 
print (distances)
print (unvisited)
print (visited)
#############################################################next visiting round 
from_point = getlowestdistancenode(distances,unvisited)
print("from point:")
print(from_point)
unvisited.remove(from_point)
visited.add(from_point)

distance_accumulated = distances[from_point] #distance of A to from_point -- TO DO: should be named distance_to_origin
for neighborn in graphaux.edges[from_point]: #from all of the edges of that point
  print (neighborn)
  
  #first check if edge it was writen a,b or b,a, and assign axuliar distance
  key = (neighborn,from_point)
  if key in graphaux.distances:
    distance_aux = graphaux.distances[neighborn,from_point]
  else:
    distance_aux= graphaux.distances[from_point,neighborn]
  #once distance is calculated first check if distance to that node is negative, if its, first time visited , if not visited, check if distance calculated is larger or lower
  if distances[neighborn]<0:
    distances[neighborn] = distance_aux+distance_accumulated    
  else: #so if its not -1, then u check if distance from that point to A + that point to the neighbor is less than the distance of that neighbor to A
    #only assing if its lower, otherwise, ignore
    if ((distance_aux+distance_accumulated )<distances[neighborn]): 
      distances[neighborn] = distance_aux+distance_accumulated 

print("final print:")
 
print (distances)
print (unvisited)
print (visited)

#############################################################next visiting round 
from_point = getlowestdistancenode(distances,unvisited)
print("from point:")
print(from_point)
unvisited.remove(from_point)
visited.add(from_point)
distance_accumulated = distances[from_point]
for neighborn in graphaux.edges[from_point]:
  print (neighborn)
  
  #first check if edge it was writen a,b or b,a, and assign axuliar distance
  key = (neighborn,from_point)
  if key in graphaux.distances:
    distance_aux = graphaux.distances[neighborn,from_point]
  else:
    distance_aux= graphaux.distances[from_point,neighborn]
  #once distance is calculated first check if distance to that node is negative, if its, first time visited , if not visited, check if distance calculated is larger or lower
  if distances[neighborn]<0:
    distances[neighborn] = distance_aux+distance_accumulated    
  else:
    #only assing if its lower, otherwise, ignore
    if ((distance_aux+distance_accumulated )<distances[neighborn]):
      distances[neighborn] = distance_aux+distance_accumulated

print("final print:")
 
print (distances)
print (unvisited)
print (visited)

"""
weighted graph:
tentative distance value to every node, 0 to initial one and infitinite to the rest
start with visiting set and unvisited set (rest of node)
start initial node, and remove it from the unvisited set,
calculate the distance to node and from those

start at node, 


"""
