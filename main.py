import networkx as nx
import matplotlib.pyplot as plt

from color_refinement import *

def create_test_graph(nodes_names, edges=None):
    # nodes names [0,1,2,3] - node labelas
    # edges [(Vi, Vj), (Vq, Vp), ...] - list of tuples with 2 elements 
    G = nx.Graph()
    G.add_nodes_from(nodes_names)
    G.add_edges_from(edges)
    return G

# real tests will be added
labels_1 = list(range(10))
edges_1 = [
    (0, 1), (0, 2), (1, 3), (1, 4), (2, 5),
    (2, 6), (3, 7), (4, 8), (5, 9), (6, 7),
    (7, 8), (8, 9)
]

node_mapping = {0: 4, 1: 7, 2: 8, 3: 1, 4: 6, 5: 3, 6: 9, 7: 2, 8: 5, 9: 0}
edges_2 = [(node_mapping[u], node_mapping[v]) for u, v in edges_1]


G1 = create_test_graph(labels_1, edges_1)
G2 = create_test_graph(list(node_mapping.values()), edges_2)

print(wl_test(G1, G2))

