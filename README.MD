
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
