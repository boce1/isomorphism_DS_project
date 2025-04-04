import networkx as nx
import matplotlib.pyplot as plt

import color_refinement

def create_test_graph(nodes_names, edges=None):
    # nodes names [0,1,2,3] - node labelas
    # edges [(Vi, Vj), (Vq, Vp), ...] - list of tuples with 2 elements 
    G = nx.Graph()
    G.add_nodes_from(nodes_names)
    G.add_edges_from(edges)
    return G

def draw_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()

def draw_2_graphs(graph1, graph2):
    pos_graph1 = nx.spring_layout(graph1, seed=color_refinement.layout_seed1)
    pos_graph2 = nx.spring_layout(graph2, seed=color_refinement.layout_seed2)

    subax1 = plt.subplot(121)
    nx.draw(graph1, pos=pos_graph1, with_labels=True)
    plt.title("Graph 1")
    subax2 = plt.subplot(122)
    nx.draw(graph2, pos=pos_graph2, with_labels=True)
    plt.title("Graph 2")
    plt.show()

# real tests will be added
# TO DO: we can create separate folder that contains tests graphs and then test them in main.py
#        it is not neccessary if theres a small number of tests graphs


#labels_1 = list(range(10))
#edges_1 = [
#    (0, 1), (0, 2), (1, 3), (1, 4), (2, 5),
#    (2, 6), (3, 7), (4, 8), (5, 9), (6, 7),
#    (7, 8), (8, 9)
#]
#G1 = create_test_graph(labels_1, edges_1)
#
#node_mapping = {0: 4, 1: 7, 2: 8, 3: 1, 4: 6, 5: 3, 6: 9, 7: 2, 8: 5, 9: 0}
#edges_2 = [(node_mapping[u], node_mapping[v]) for u, v in edges_1]
#G2 = create_test_graph(list(node_mapping.values()), edges_2)
#
#draw_2_graphs(G1, G2)
#print(color_refinement.wl_test(G1, G2, visualize=True))



G1a = nx.Graph()
G1a.add_nodes_from(range(10))
G1a.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,0),
                    (0,2),(1,3),(2,4),(3,5),(4,6)])

# Graph G1b (non-isomorphic to G1a)
G1b = nx.Graph()
G1b.add_nodes_from(range(10))
G1b.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,0),
                    (0,5),(1,6),(2,7),(3,9),(4,9)])

#draw_graph(G1)
draw_2_graphs(G1a, G1b)
print(color_refinement.wl_test(G1a, G1b, visualize=True))

