import color_refinement
import vf_2
from test_graphs import test1, test2, test3, test4, test5, test6, test7, test8, draw_2_graphs, draw_graph

def format_result(test_name, is_isomorphic):
    if is_isomorphic:
        print(f"{test_name} : Graphs are isomorphic")
    else:
        print(f"{test_name} : Graphs are NOT isomorphic")

tests = [test1, test2, test3, test4, test5, test6, test7, test8]
for i in range(len(tests)):
    test = tests[i]
    result_vf_2 = vf_2.vf2_isomorphism(*test)
    result_color_refinement = color_refinement.wl_test(*test) # visualize=False
    # add result for third alg

    draw_2_graphs(test[0], test[1])

    print(f"Test {i + 1}:")
    format_result("VF2", result_vf_2)
    format_result("Color Refinement", result_color_refinement)
    
    print("---------------------\n")
