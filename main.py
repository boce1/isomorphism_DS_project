import networkx as nx
import matplotlib.pyplot as plt

from color_refinement import *

G1 = nx.erdos_renyi_graph(10, 0.5)
G2 = nx.erdos_renyi_graph(10, 0.5)

result = wl_test(G1, G2)
print("Graphs are isomorphic:", result)

nx.draw(G1, with_labels=True)
plt.show()
nx.draw(G2, with_labels=True)
plt.show()