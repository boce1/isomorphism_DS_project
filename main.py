import color_refinement
from test_graphs import *

draw_2_graphs(*test8)

print(color_refinement.wl_test(*test8, visualize=True, node_size=150))