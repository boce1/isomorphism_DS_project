# # # isomorphic graphs
isomprphic_test1 = {
    "graph1" : {
        "labels" : [chr(ord("a") + i) for i in range(5)], # a-e
        "edges" : [("a", "b"), ("a", "c"), ("b", "c"), ("b", "e"), ("c", "d"), ("d", "e")]
    },
    "graph2": {
        "labels" : list(range(1, 6)),
        "edges" : [(1,2), (1,5), (2,3), (2,5), (3,4), (4,5)]
    }
}

isomprphic_test2 = {
    "graph1" : {
        "labels" : list(range(0, 10)),
        "edges" : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0),
             (0, 5), (2, 7), (3, 8)]
    },
    "graph2": {
        "labels" : list(range(0, 10)),
        "edges" : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0),
             (0, 5), (2, 7), (3, 8)]
    }
}

isomprphic_test3 = {
    "graph1" : {
        "labels" : list(range(1, 21)),
        "edges" : [(i, i+1) for i in range(1, 20)] + [(20, 1)] + 
                    [(5,15), (9,17), (11, 3), (14, 3), (11, 15)]
    },
    "graph2": {
        "labels" : list(range(1, 21)),
        "edges" : [(i, i+1) for i in range(1, 20)] + [(20, 1)] + 
                    [(5,15), (9,17), (11, 3), (14, 3), (11,15)]
    }
}
# # #

# # # non-isomorphic graphs
non_isomprphic_test3 = {
    "graph1" : {
        "labels" : list(range(1, 21)),
        "edges" : [(i, i+1) for i in range(1, 20)] + [(20, 1)] + 
                    [(1, 5), (2, 8), (8, 10), (4, 12), (7, 15), (7, 18), (9, 20), (11, 14), (13, 16), (17, 19)]
    },
    "graph2": {
        "labels" : list(range(1, 21)),
        "edges" : [(i, i+1) for i in range(1, 20)] + [(20, 1)] + 
                    [(1, 5), (2, 8), (3, 10), (4, 12), (6, 15), (7, 18), (9, 20), (11, 14), (13, 16), (17, 19)]
    }
}
# # #
