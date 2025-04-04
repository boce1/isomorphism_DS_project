import color_refinement
from test_graphs import *

draw_2_graphs(test6[0], test6[1])

print(color_refinement.wl_test(test6[0], test6[1], visualize=True))