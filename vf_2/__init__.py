import networkx as nx

def vf2_isomorphism(graphs):
    '''
    This is a function that uses the vf2 algorithm, which is already
    provided by networkx in its default functions that check for isomorphism.
    A hand written implementation, not relying on networkx is coming soon.
    '''
    
    G1 = graphs[0]
    G2 = graphs[1]
    GM = nx.algorithms.isomorphism.GraphMatcher(G1, G2)
    print(f"The graphs are {"isomorphic" if GM.is_isomorphic() else "not isomorphic"}")
    print(f"\nMapping of the two graphs is\n{GM.mapping}")