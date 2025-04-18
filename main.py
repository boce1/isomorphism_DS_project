from networkx.algorithms import isomorphism
import color_refinement
import vf_2
from test_graphs import test1, test2, test3, test4, test5, test6, test7, test8, test9, draw_2_graphs, draw_graph

def format_result(test_name, is_isomorphic):
    if is_isomorphic:
        print(f"{test_name} : Graphs are isomorphic")
    else:
        print(f"{test_name} : Graphs are NOT isomorphic")

tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9]
for i in range(len(tests)): # skip the last 2 test, VF2 calculation is too long
    test = tests[i]

    if i not in (6,7): # test 7 and 8
        result_vf_2 = vf_2.vf2_isomorphism(*test)
    else:
        GM = isomorphism.GraphMatcher(*test)
        result_vf_2 = GM.is_isomorphic()
        
    result_color_refinement = color_refinement.wl_test(*test)
    # add result for third alg

    draw_2_graphs(*test)
    print(f"Test {i + 1}:")


    format_result("VF2", result_vf_2)
    format_result("Color Refinement", result_color_refinement)

    print("---------------------")

# test 9 - 1-WL doesnt always recognize non-isomorphic graphs. The solution is to go to high order extentions. Nodes need to have multiple characteristics. 