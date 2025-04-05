"""
tests 1,2,3,4 are isomorphic
tests 5,6,7,8 are non-isomprphic
"""

import networkx as nx
import matplotlib.pyplot as plt
from .names_edges import *

layout_seed1 = 0
layout_seed2 = 1
default_node_size = 300

def create_test_graph(nodes_names, edges=None):
    # nodes names [0,1,2,3] - node labels
    # edges [(Vi, Vj), (Vq, Vp), ...] - list of tuples with 2 elements 
    G = nx.Graph()
    G.add_nodes_from(nodes_names)
    G.add_edges_from(edges)
    return G

def draw_graph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()

def draw_2_graphs(graph1, graph2, node_size=default_node_size):
    pos_graph1 = nx.spring_layout(graph1, seed=layout_seed1)
    pos_graph2 = nx.spring_layout(graph2, seed=layout_seed2)

    subax1 = plt.subplot(121)
    nx.draw(graph1, pos=pos_graph1, with_labels=True, node_size=node_size)
    plt.title("Graph 1")
    subax2 = plt.subplot(122)
    nx.draw(graph2, pos=pos_graph2, with_labels=True, node_size=node_size)
    plt.title("Graph 2")
    plt.show()

# # #
test1_g1 = create_test_graph(isomorphic_test1["graph1"]["labels"], isomorphic_test1["graph1"]["edges"])
test1_g2 = create_test_graph(isomorphic_test1["graph2"]["labels"], isomorphic_test1["graph2"]["edges"])
test1 = (test1_g1, test1_g2)

test2_g1 = create_test_graph(isomorphic_test2["graph1"]["labels"], isomorphic_test2["graph1"]["edges"])
test2_g2 = create_test_graph(isomorphic_test2["graph2"]["labels"], isomorphic_test2["graph2"]["edges"])
test2 = (test2_g1, test2_g2)

test3_g1 = create_test_graph(isomorphic_test3["graph1"]["labels"], isomorphic_test3["graph1"]["edges"])
test3_g2 = create_test_graph(isomorphic_test3["graph2"]["labels"], isomorphic_test3["graph2"]["edges"])
test3 = (test3_g1, test3_g2)

test4_g1 = create_test_graph(isomorphic_test4["graph1"]["labels"], isomorphic_test4["graph1"]["edges"])
test4_g2 = create_test_graph(isomorphic_test4["graph2"]["labels"], isomorphic_test4["graph2"]["edges"])
test4 = (test4_g1, test4_g2)
# # #

# # #
test5_g1 = create_test_graph(non_isomorphic_test1["graph1"]["labels"], non_isomorphic_test1["graph1"]["edges"])
test5_g2 = create_test_graph(non_isomorphic_test1["graph2"]["labels"], non_isomorphic_test1["graph2"]["edges"])
test5 = (test5_g1, test5_g2)

test6_g1 = create_test_graph(non_isomorphic_test2["graph1"]["labels"], non_isomorphic_test2["graph1"]["edges"])
test6_g2 = create_test_graph(non_isomorphic_test2["graph2"]["labels"], non_isomorphic_test2["graph2"]["edges"])
test6 = (test6_g1, test6_g2)

test7_g1 = create_test_graph(non_isomorphic_test3["graph1"]["labels"], non_isomorphic_test3["graph1"]["edges"])
test7_g2 = create_test_graph(non_isomorphic_test3["graph2"]["labels"], non_isomorphic_test3["graph2"]["edges"])
test7 = (test7_g1, test7_g2)

test8_g1 = create_test_graph(non_isomorphic_test4["graph1"]["labels"], non_isomorphic_test4["graph1"]["edges"])
test8_g2 = create_test_graph(non_isomorphic_test4["graph2"]["labels"], non_isomorphic_test4["graph2"]["edges"])
test8 = (test8_g1, test8_g2)
# # #