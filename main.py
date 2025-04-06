import color_refinement
from test_graphs import *

# draw_2_graphs(*test1)
# print("Test 1, 1-WL test: ", color_refinement.wl_test(*test1, visualize=True))
# 
# draw_2_graphs(*test3)
# print("Test 3, 1-WL test: ", color_refinement.wl_test(*test3, visualize=True))

draw_2_graphs(*test4, node_size=150)
print("Test 4, 1-WL test: ", color_refinement.wl_test(*test4, visualize=True, node_size=150))