def refine_labels(graph, node_labels):
    '''
    structure_labels is dict that maps node to its neighbourhood structure.
    color_label is dict that maps neighbourhood structure to its unique hash value.

    if 2 nodes have the same previous label, and same neighbourhood structure, they will have same hash value.
    '''
    new_labels = {}

    color_labels = {}
    structure_labels = {}
    label_value = 1
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

def wl_test(G1, G2, max_iterations=20):
    if len(G1.nodes) != len(G2.nodes) or len(G1.edges) != len(G2.edges):
        return False
    
    g1_labels = {node : G1.degree(node) for node in G1.nodes}
    g2_labels = {node : G2.degree(node) for node in G2.nodes}

    for i in range(max_iterations):
        g1_labels = refine_labels(G1, g1_labels)
        g2_labels = refine_labels(G2, g2_labels)

        print(g2_labels)

        if sorted(g1_labels.values()) == sorted(g2_labels.values()):
            return True

    return False


# G1.nodes[0]["color"] = "blue"
# 
# node_colors = [G1.nodes[n].get("color", "lightgray") for n in G1.nodes()]
# nx.draw(G1, with_labels=True, node_color=node_colors, edge_color="black", node_size=500)
# #nx.draw(G1, with_labels=True)
# plt.show()