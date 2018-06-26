import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

G = nx.karate_club_graph()
# adjacency matrix
A = nx.to_numpy_matrix(G)
# nodes degree vector
k = np.sum(A,axis=0)
# two times total number of edges
twom = np.sum(k)
# modularity matrix
B = A - np.outer(k,k)/twom
x,v = eigh(B)
vector = v.T
# leading eigenvector
print(vector[-1])
lead_vector = vector[-1]
vector = list(lead_vector.flat)
color_map = []
for i in range(len(G)):
    if vector[i] >= 0:
        color_map.append('red')
    else:
        color_map.append('green')

fig = plt.figure()
nx.draw(G,node_color = color_map,with_labels = True)
plt.show(block=True)
plt.interactive(False)
fig.savefig("karate-club.png")




