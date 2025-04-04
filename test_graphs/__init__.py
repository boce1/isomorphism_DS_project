import networkx as nx
import matplotlib.pyplot as plt
from .names_edges import *

layout_seed1 = 0
layout_seed2 = 1

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

def draw_2_graphs(graph1, graph2):
    pos_graph1 = nx.spring_layout(graph1, seed=layout_seed1)
    pos_graph2 = nx.spring_layout(graph2, seed=layout_seed2)

    subax1 = plt.subplot(121)
    nx.draw(graph1, pos=pos_graph1, with_labels=True)
    plt.title("Graph 1")
    subax2 = plt.subplot(122)
    nx.draw(graph2, pos=pos_graph2, with_labels=True)
    plt.title("Graph 2")
    plt.show()


test1_g1 = create_test_graph(isomprphic_test1["graph1"]["labels"], isomprphic_test1["graph1"]["edges"])
test1_g2 = create_test_graph(isomprphic_test1["graph2"]["labels"], isomprphic_test1["graph2"]["edges"])
test1 = (test1_g1, test1_g2)

test2_g1 = create_test_graph(isomprphic_test2["graph1"]["labels"], isomprphic_test2["graph1"]["edges"])
test2_g2 = create_test_graph(isomprphic_test2["graph2"]["labels"], isomprphic_test2["graph2"]["edges"])
test2 = (test2_g1, test2_g2)

test3_g1 = create_test_graph(isomprphic_test3["graph1"]["labels"], isomprphic_test3["graph1"]["edges"])
test3_g2 = create_test_graph(isomprphic_test3["graph2"]["labels"], isomprphic_test3["graph2"]["edges"])
test3 = (test3_g1, test3_g2)

# add test4 and test5 as the easy and medium difficulty level non isomprphic graphs
# 
#  

test6_g1 = create_test_graph(non_isomprphic_test3["graph1"]["labels"], non_isomprphic_test3["graph1"]["edges"])
test6_g2 = create_test_graph(non_isomprphic_test3["graph2"]["labels"], non_isomprphic_test3["graph2"]["edges"])
test6 = (test6_g1, test6_g2)