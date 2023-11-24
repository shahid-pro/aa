from collections import deque
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt                 
class Graph:
    def __init__(self,num_nodes):
        self.num_nodes=num_nodes
        self.adjlist=[[] for _ in range(num_nodes)]
    def edge(self,node1,node2):
        if node1<self.num_nodes and node2<self.num_nodes:
            self.adjlist[node1].append(node2)
            self.adjlist[node2].append(node1)
        else :
            if node1>=self.num_nodes and node2>=self.num_nodes:
                print(f"{node1} & {node2} are invalid nodes")
            else:
                print(f"{max(node1,node2)} is an invalid node")
    def adj(self):
        Matrix=np.zeros((self.num_nodes,self.num_nodes))
        for i in range(self.num_nodes):
            for j in self.adjlist[i]:
                Matrix[i][j]=1
        return Matrix
    def print(self):
        adjmat=self.adj()
        graph=nx.from_numpy_array(adjmat)
        nx.draw(graph, with_labels=True)
        plt.show()
    def connected(self, node):
        connected_nodes=[]
        for n in self.adjlist[node]:
            connected_nodes.append(n)
        return connected_nodes
    def neighbor(self, node):
        return self.adjlist[node]
def has_cycle(graph):
    is_visited=set()
    for node in range(graph.num_nodes):
        if node not in is_visited:
            if bfs_has_cycle(graph,node,is_visited):
                return True
    return False
def bfs_has_cycle(graph,start_node,is_visited):
    queue=deque()
    queue.append((start_node,None))
    while queue:
        current_node,parent_node=queue.popleft()
        is_visited.add(current_node)
        for neighbor in graph.neighbor(current_node):
            if neighbor not in is_visited:
                queue.append((neighbor,current_node))
            elif neighbor!=parent_node:
                return True
    return False
g=Graph(6)
g.edge(0,1)
g.edge(0,4)
g.edge(1,2)
g.edge(1,3)
g.edge(2,3)
g.edge(3,4)
g.edge(7,8)
g.edge(1,8)
print(g.adjlist)
has_cycle(g)
def search():
    for n in range(g.num_nodes):
        connectednodes=g.connected(n)
        if connectednodes==[]:
            print(f"{n} is not connected")
        else:
            print(f"{n} is connected")
search()
has_cycle_result = has_cycle(g)
if has_cycle_result:
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
g.print()
h=Graph(6)
h.edge(0,1)
h.edge(0,4)       
h.edge(2,3)
h.edge(3,4)
h.edge(1,5)
print(h.adjlist)
has_cycle(h)
def search():
    for n in range(h.num_nodes):
        connectednodes=h.connected(n)
        if connectednodes==[]:
            print(f"{n} is not connected")
        else:
            print(f"{n} is connected")
search()
has_cycle_result = has_cycle(h)
if has_cycle_result:
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
h.print()