#import networkx as nx

def refine_labels(graph, node_labels):
    new_labels = {}
    for node in graph.nodes:
        neighbors = sorted([node_labels[neighbor] for neighbor in graph.neighbors(node)])
        new_labels[node] = tuple([node_labels[node]] + neighbors)
    return new_labels

def wl_test(graph1, graph2, max_iterations=10):
    # Initialize node labels as the degree of each node (or any initial label)
    node_labels1 = {node: (graph1.degree(node),) for node in graph1.nodes}
    node_labels2 = {node: (graph2.degree(node),) for node in graph2.nodes}
    
    # Check if both graphs have the same number of nodes and edges
    if len(graph1.nodes) != len(graph2.nodes) or len(graph1.edges) != len(graph2.edges):
        return False
    
    # Run the Weisfeiler-Lehman test for a set number of iterations
    for _ in range(max_iterations):
        node_labels1 = refine_labels(graph1, node_labels1)
        node_labels2 = refine_labels(graph2, node_labels2)
        
        # Check if the labels are the same for both graphs
        if sorted(node_labels1.values()) != sorted(node_labels2.values()):
            return False

    return True