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
    """

    all_trees, adjacency = gar.generate_all_rotations(n)
    num_trees = len(all_trees)
    distance_matrix = np.full((num_trees, num_trees), np.inf)