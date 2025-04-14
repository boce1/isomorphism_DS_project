import color_refinement
import vf_2
import networkx as nx
from test_graphs import test1, test2, test3, test4, test5, test6, test7, test8, draw_2_graphs, draw_graph

# test algs here
# TO DO: when all algs are finished, write all test for all algs

tests = [test1, test2, test3, test4, test5, test6, test7, test8]
for i in range(len(tests)):
    test = tests[i]
    result = vf_2.vf2_isomorphism(test[0], test[1])
    print(f"Graph from test{i + 1} is {"ISOMORPHIC" if result else "NOT ISOMORPHIC"}")