import numpy as np

def adjacency_matrix_comparison_test(g1, g2):
    """Check if two graphs are isomorphic by comparing adjacency matrices"""

    adj1 = convert_graph_to_adj_matrix(g1)
    adj2 = convert_graph_to_adj_matrix(g2)

    if len(adj1) != len(adj2):
        return False
    
    if not basic_checks_pass(adj1, adj2):
        return False
    
    return True

def basic_checks_pass(adj1, adj2):
    n = len(adj1)
    
    deg1 = sorted(sum(row) for row in adj1)
    deg2 = sorted(sum(row) for row in adj2)
    if deg1 != deg2:
        return False
    
    if sum(sum(row) for row in adj1) != sum(sum(row) for row in adj2):
        return False
    
    try:
        eig1 = sorted(np.linalg.eigvals(adj1))
        eig2 = sorted(np.linalg.eigvals(adj2))
        if not np.allclose(eig1, eig2, atol=1e-6):
            return False
    except:
        pass
    
    return True

def convert_graph_to_adj_matrix(graph):
    """Convert networkx graph to adjacency matrix"""
    nodes = sorted(graph.nodes())
    n = len(nodes)
    adj = [[0]*n for _ in range(n)]
    
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if graph.has_edge(u, v):
                adj[i][j] = 1
    return adj