"""
Docstring for BTR.rotation_distance

Given an associahedron graph of binary trees of size n, this module computes the
rotation distance matrix between all pairs of binary trees. The rotation distance
between two binary trees is defined as the minimum number of rotations required to
transform one tree into the other. 

We will perform a breadth-first search (BFS) from each tree to compute the shortest
path to all other trees in the graph, thereby constructing the distance matrix.
"""

from src.structs.binaryTree import BinaryTree
from src.BTR import generate_all_rotations as gar
from collections import deque
import numpy as np

def compute_rotation_distance_matrix(n):
    """
    Docstring for compute_rotation_distance_matrix
    
    :param n: Number of nodes in the binary trees.
    :return: A 2D numpy array representing the rotation distance matrix.
    :return: The rotation diameter of the graph.
    """

    all_trees, adjacency = gar.generate_all_rotations(n)
    num_trees = len(all_trees)
    distance_matrix = np.full((num_trees, num_trees), np.inf)
    max_distance = num_trees - 1
    np.fill_diagonal(distance_matrix, 0)
    tree_index = {str(tree.preorder_traversal()): idx for idx, tree in enumerate(all_trees)}
    for idx, tree in enumerate(all_trees):
        start_preorder = str(tree.preorder_traversal())
        queue = deque([(start_preorder, 0)])
        visited = set()

        while queue:
            current_preorder, dist = queue.popleft()
            if current_preorder in visited:
                continue
            visited.add(current_preorder)

            current_idx = tree_index[current_preorder]
            distance_matrix[idx][current_idx] = dist

            for neighbor in adjacency.get(current_preorder, []):
                if neighbor not in visited:
                    queue.append((neighbor, dist + 1))
                    if dist + 1 > max_distance:
                        max_distance = dist + 1
    return distance_matrix, max_distance

if __name__ == "__main__":
    n = 3
    distance_matrix, max_distance = compute_rotation_distance_matrix(n)
    all_trees, _ = gar.generate_all_rotations(n)
    print(f"Rotation distance matrix for binary trees of size {n}:")
    for i, row in enumerate(distance_matrix):
        for tree in all_trees:
            print(f"Distance from tree {all_trees[i].preorder_traversal()} to tree {tree.preorder_traversal()}: {row[all_trees.index(tree)]}")