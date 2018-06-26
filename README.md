# Karate-Club-Clustering-methods-by-Mark-Newman
Application of eigenvector-based community clustering method by Mark Newman in Python
'Modularity and community structure in networks' by Mark Newman 2006
https://arxiv.org/abs/physics/0602124
Here is one example in python using eigenvector method to do community detection.


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
# get karate club garph
G = nx.karate_club_graph()
# adjacency matrix
A = nx.to_numpy_matrix(G)
# nodes degree vector
k = np.sum(A,axis=0)
# two times of total no. of edegs
twom = np.sum(k)
# modularity matrix
B = A - np.outer(k,k)/twom
# eigenvalue and eigenvector
x,v = eigh(B)
# leading eigenvector
print(vector[-1])
lead_vector = vector[-1]
# assign different colors to nodes
vector = list(lead_vector.flat)
color_map = []
for i in range(len(G)):
    if vector[i] >= 0:
        color_map.append('red')
    else:
        color_map.append('green')
nx.draw(G,node_color = color_map,with_labels = True)

plt.show(block=True)
plt.interactive(False)
