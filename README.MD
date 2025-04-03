
# Isomorphism Algorithms

This project contains implementations of three different algorithms for graph isomorphism checking. The algorithms included are:

1. **Color Refinement (Weisfeiler-Lehman Test, 1-WL)** 
2. **Marking Adjacency Matrix with BFS/DFS**  
3. **VF2 Algorithm**

Each algorithm is implemented in its own separate package, and the main test script is located in `main.py`.

## Project Structure

- `color_refinement/` - Contains the implementation for the Color Refinement algorithm.
- `bfs_dfs/` - Contains the implementation for marking the adjacency matrix using BFS or DFS.
- `vf2/` - Contains the implementation for the VF2 algorithm.
- `main.py` - The main script that runs the tests for all three algorithms.

Each algorithm is implemented by a different contributor, with each contributing one algorithm. The main test script is located in main.py.

Боян Зарев, факултетен номер: 123222004 -`color_refinement/`
Светлин Иванов, факултетен номер: 121222088 - `adjacency_matrix_comparison/`
Ивайлов Николов, факултетен номер: 121222009 - `vf_2`

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

2. Install the necessary dependencies (NOTE: python3.x must be added to the PATH variable):
   ```bash
   pip install networkx[default]
   pip install matplotlib
   ```

3. Run the main test script:
   ```bash
   python main.py
   ```

This will execute the tests for all three algorithms and print the results.