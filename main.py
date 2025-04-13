import color_refinement
import vf_2
from test_graphs import test1, test2, test3, test4, test5, test6, test7, test8

# test algs here
# TO DO: when all algs are finished, write all test for all algs

# tests = [test1, test2, test3, test4, test5, test6, test7, test8]
# for i in range(1, len(tests) + 1):
#     vf_2.G1 = (set(tests[i - 1][0].nodes), set(tests[i - 1][0].edges))
#     vf_2.G2 = (set(tests[i - 1][1].nodes), set(tests[i - 1][1].edges))
#     result = vf_2.vf2_isomorphism(set(), 300)
#     print(result)
#     print(f"Graph from test{i} is {"ISOMORPHIC" if result[0] else "NOT ISOMORPHIC"}")
#     print(f"\nMapping is: {[x for x in result[1]]}")

vf_2.G1 = (set([1, 2, 3]), set([(1, 2), (2, 3)]))
vf_2.G2 = (set([1, 2, 3]), set([(2, 1), (1, 3)]))
result = vf_2.vf2_isomorphism(set(), 300)
print(result)