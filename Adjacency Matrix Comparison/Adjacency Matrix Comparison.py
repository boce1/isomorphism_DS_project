import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def is_bipartite_graph(adj):

    return len(adj) != len(adj[0]) if adj else False

def plot_graph(adj_matrix):
    if len(adj_matrix) != len(adj_matrix[0]):
        print(f"Error Matrix is not squered.")
        return
    
    G = nx.Graph() if not nx.is_directed(nx.DiGraph(np.array(adj_matrix))) else nx.DiGraph()
    n = len(adj_matrix)
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                G.add_edge(i, j)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
    plt.show()

def are_isomorphic(adj1, adj2):

    if len(adj1) != len(adj1[0]) or len(adj2) != len(adj2[0]):
        return False
    
    n = len(adj1)
    if n != len(adj2):
        return False
    
    for perm in permutations(range(n)):
        if all(adj1[perm[i]][perm[j]] == adj2[i][j] for i in range(n) for j in range(n)):
            return True
    return False

adj1 = [[0, 1, 0, 0, 1],  
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 0]]

adj2 = [[1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 0]]

adj3 = [[0, 1, 1],  
        [0, 0, 0],
        [1, 0, 0]]

plot_graph(adj1)
plot_graph(adj2)
plot_graph(adj3)