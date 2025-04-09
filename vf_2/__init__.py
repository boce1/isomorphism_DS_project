import networkx as nx

# def vf2_isomorphism(graphs):
#     '''
#     This is a function that uses the vf2 algorithm, which is already
#     provided by networkx in its default functions that check for isomorphism.
#     A hand written implementation, not relying on networkx is coming soon.
#     '''
    
#     G1 = graphs[0]
#     G2 = graphs[1]
#     GM = nx.algorithms.isomorphism.GraphMatcher(G1, G2)
#     print(f"The graphs are {"isomorphic" if GM.is_isomorphic() else "not isomorphic"}")
#     print(f"\nMapping of the two graphs is\n{GM.mapping}")
G1 = (set(),set())
G2 = (set(),set())

def vf2_isomorphism(mapping):
    if G1.get_nodes() == set([x[0] for x in mapping]):
        return (True, mapping)
    else:
        candidate_pairs = compute_Pm()
        for pair in candidate_pairs:
            extended_mapping = extend_mapping(mapping, pair)
            if cons(extended_mapping) and not cut(extended_mapping):
                vf2_isomorphism(G1, G2, extended_mapping)

def extend_mapping(m, p):
    if p[0] in (G1[0] - set([x[0] for x in m])) and p[1] in (G2[0] - set([x[1] for x in m])):
        return m.append(p)
    else:
        return m

def compute_Pm(m):
    result = []
    for node_1 in G1[0]:
        for node_2 in G2[0]:
            if (node_1 , node_2) not in m:
                result.append((node_1, node_2))
    return result