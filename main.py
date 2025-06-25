from networkx.algorithms import isomorphism
import color_refinement
import vf_2
import adjacency_matrix_comparison
from test_graphs import test1, test2, test3, test4, test5, test6, test7, test8, test9, draw_2_graphs

def format_result(test_name, is_isomorphic):
    if is_isomorphic:
        print(f"{test_name} : Graphs are isomorphic")
    else:
        print(f"{test_name} : Graphs are NOT isomorphic")

tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9]
for i in range(len(tests)):
    test = tests[i]

    if i not in (6,7): # test 7 and 8
        result_vf_2 = vf_2.vf2_isomorphism(*test)
    else:
        GM = isomorphism.GraphMatcher(*test)
        result_vf_2 = GM.is_isomorphic()
        
    result_color_refinement = color_refinement.wl_test(*test)
    result_adj_matrix = adjacency_matrix_comparison.adjacency_matrix_comparison_test(*test)

    draw_2_graphs(*test)
    print(f"Test {i + 1}:")

    format_result("VF2", result_vf_2)
    format_result("Color Refinement", result_color_refinement)
    format_result("Adjacency Matrix", result_adj_matrix)

    print("---------------------")
    
    if i == len(tests) - 1:
        input("Press Enter to close")