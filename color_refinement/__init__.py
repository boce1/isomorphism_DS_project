import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import CSS4_COLORS
from random import seed, shuffle
from test_graphs import layout_seed1, layout_seed2

def refine_labels(graph, node_labels):
    '''
    structure_labels is dict that maps node to its neighbourhood structure.
    color_label is dict that maps neighbourhood structure to its unique hash value.

    if 2 nodes have the same previous label, and same neighbourhood structure, they will have same hash value.
    '''
    new_labels = {}

    color_labels = {}
    structure_labels = {}
    label_value = 0
    for node in graph.nodes:
        neighbors_coloring = sorted([node_labels[neighbor] for neighbor in graph.neighbors(node)])
        color = (node_labels[node],) + tuple(neighbors_coloring) # adds labels of neighbours to the current label of the given node and form it like a tuple
        # the purpose of this is to create unique labels for the nodes, having in consideration structure of neighbourhood
        structure_labels[node] = color

        if color not in color_labels:  # creating new "hash" value for new label
            color_labels[color] = label_value
            label_value += 1

    for node in graph.nodes:
        new_labels[node] = color_labels[structure_labels[node]]

    return new_labels



def wl_test(G1, G2, max_iterations=10, visualize=False):
    '''
    Computes 1-WL test, return True if graphs are isomorphic, False when they are not.
    G1, G2 are graphs parameters.
    max_iterations is default number of iteration that algorythm will go through.

    visualize is parameter that specify if each iteration will be visualized with matplotlib.
    When True it will visualize the given phase of the 1-WL test and algorythm will NOT continue UNTIL user close the window 
    in wich 2 graphs have been visualized.

    The initial labels of nodes are their degrees.
    '''
    if len(G1.nodes) != len(G2.nodes) or len(G1.edges) != len(G2.edges):
        return False
    
    g1_labels = {node : G1.degree(node) for node in G1.nodes}
    g2_labels = {node : G2.degree(node) for node in G2.nodes}

    if visualize:
            draw_color_2_graph(G1, g1_labels, G2, g2_labels)

    for i in range(max_iterations):
        g1_labels = refine_labels(G1, g1_labels)
        g2_labels = refine_labels(G2, g2_labels)


        if visualize:
            draw_color_2_graph(G1, g1_labels, G2, g2_labels)


        if sorted(g1_labels.values()) == sorted(g2_labels.values()):
            return True
    return False




# function for visualizing

seed(1)
css_colors = list(CSS4_COLORS.keys())
shuffle(css_colors)

def draw_color_graph(graph, labels):
    colors = []
    for node in graph.nodes:
        color = css_colors[labels[node] % len(css_colors)]
        colors.append(color)
    
    pos = nx.spring_layout(graph, seed=layout_seed1)
    nx.draw(graph, pos=pos, with_labels=True, node_color=colors)
    plt.show()

def draw_color_2_graph(graph1, graph1_labels, graph2, graph2_labels):
    colors_graph1 = []
    colors_graph2 = []

    for node in graph1.nodes:
        color = css_colors[graph1_labels[node] % len(css_colors)]
        colors_graph1.append(color)

    for node in graph2.nodes:
        color = css_colors[graph2_labels[node] % len(css_colors)]
        colors_graph2.append(color)
    
    pos_graph1 = nx.spring_layout(graph1, seed=layout_seed1)
    pos_graph2 = nx.spring_layout(graph2, seed=layout_seed2)

    plt.figure(figsize=(10, 7))
    subax1 = plt.subplot(221)
    nx.draw(graph1, pos=pos_graph1, with_labels=True, node_color=colors_graph1)
    plt.title("Graph 1")

    subax2 = plt.subplot(222)
    nx.draw(graph2, pos=pos_graph2, with_labels=True, node_color=colors_graph2)
    plt.title("Graph 2")


    color1_occurrences = {}
    for c in colors_graph1:
        if c not in color1_occurrences:
            color1_occurrences[c] = 1
        else:
            color1_occurrences[c] += 1
    color2_occurrences = {}
    for c in colors_graph2:
        if c not in color2_occurrences:
            color2_occurrences[c] = 1
        else:
            color2_occurrences[c] += 1

    colors1_bar = sorted(color1_occurrences.keys(), key=lambda x: color1_occurrences[x])
    colors2_bar = sorted(color2_occurrences.keys(), key=lambda x: color2_occurrences[x])

    subax3 = plt.subplot(223)
    plt.bar(colors1_bar, [color1_occurrences[c] for c in colors1_bar], color=colors1_bar, width=0.6)
    plt.xticks(rotation=-45, fontsize=8, ha='left')
    plt.ylabel("Occurrences")
    plt.ylim(0, len(graph1))
    plt.title("Graph 1 Color chart")
    plt.margins(x=0.05)

    subax4 = plt.subplot(224)
    plt.bar(colors2_bar, [color2_occurrences[c] for c in colors2_bar], color=colors2_bar, width=0.6)
    plt.xticks(rotation=-45, fontsize=8, ha='left')
    plt.ylabel("Occurrences")
    plt.ylim(0, len(graph2))
    plt.title("Graph 2 Color chart")
    plt.margins(x=0.05)

    plt.show()