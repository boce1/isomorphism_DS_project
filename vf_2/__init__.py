def vf2_isomorphism(graph1, graph2):
    """
    Check if two graphs are isomorphic using the VF2 algorithm.

    Parameters:
        graph1 (Graph): The first graph.
        graph2 (Graph): The second graph.

    Returns:
        bool: True if the graphs are isomorphic, False otherwise.
    """
    if len(graph1.nodes) != len(graph2.nodes):
        return False

    def is_feasible(mapping, u, v):
        # Check if the mapping is consistent with the graph structure
        for mapped_u, mapped_v in mapping.items():
            if v in mapping.values():
                return False
            if u in mapping.keys():
                return False
            if mapped_v in graph2.neighbors(v) and mapped_u not in graph1.neighbors(u):
                return False
        return True

    def match(mapping):
        if len(mapping) == len(graph1.nodes):
            return True

        for u in graph1.nodes:
            if u not in mapping:
                for v in graph2.nodes:
                    if v not in mapping.values() and is_feasible(mapping, u, v):
                        mapping[u] = v
                        if match(mapping):
                            return True
                        del mapping[u]
                return False
        return False

    return match({})
