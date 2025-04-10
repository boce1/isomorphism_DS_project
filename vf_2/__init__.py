import networkx as nx
import itertools

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

def vf2_isomorphism(mapping, iterations):
    if iterations <= 0:
        return (False, mapping)
    if G1[0] == set([x[0] for x in mapping]):
        return (True, mapping)
    else:
        candidate_pairs = compute_Pm(mapping)
        for pair in candidate_pairs:
            extended_mapping = extend_mapping(mapping, pair)
            if cons(mapping, pair) and not cut(mapping, pair):
                vf2_isomorphism(extended_mapping, iterations - 1)

def extend_mapping(m, p):
    if p[0] in (G1[0] - set([x[0] for x in m])) and p[1] in (G2[0] - set([x[1] for x in m])):
        return m.add(p)
    else:
        return m

def compute_Pm(m):
    G1_nodes = set([x for x in G1[0] - set([y[0] for y in m])])
    G2_nodes = set([x for x in G2[0] - set([y[1] for y in m])])
    T1 = set([x for x in G1_nodes if ((x, y[0]) in G1[1] for y in m)])
    T2 = set([x for x in G2_nodes if ((x, y[1]) in G2[1] for y in m)])

    if not T1 and not T2:
        return itertools.product(T1, T2)
    else:
        return itertools.product(G1_nodes, G2_nodes)

def cons(m, p):
    gamma_1 = set([x for x in G1[0] if (p[0], x) in G1[1]])
    gamma_2 = set([x for x in G2[0] if (p[1], x) in G2[1]])
    return set([x for x in gamma_2.intersection(set([y[1] for y in m])) if (p[0], [z[0] for z in m if z[1] == x][0]) in G1[1]]) \
    and set([x for x in gamma_1.intersection(set([y[0] for y in m])) if (p[1], [z[1] for z in m if z[0] == x][0]) in G2[1]])

def cut(m, p):
    G1_nodes = set([x for x in G1[0] - set([y[0] for y in m])])
    G2_nodes = set([x for x in G2[0] - set([y[1] for y in m])])
    T1 = set([x for x in G1_nodes if ((x, y[0]) in G1[1] for y in m)])
    T2 = set([x for x in G2_nodes if ((x, y[1]) in G2[1] for y in m)])
    T1_tilde = (G1[0] - set([x[0] for x in m])) - T1
    T2_tilde = (G2[0] - set([x[1] for x in m])) - T2
    gamma_1 = set([x for x in G1[0] if (p[0], x) in G1[1]])
    gamma_2 = set([x for x in G2[0] if (p[1], x) in G2[1]])
    return len(gamma_2.intersection(T2)) < len(gamma_1.intersection(T1)) \
    and len(gamma_2.intersection(T2_tilde)) < len(gamma_1.intersection(T1_tilde))
