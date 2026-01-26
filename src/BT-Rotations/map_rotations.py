"""
Docstring for BT-Rotations.map_rotations
This module aims to create the rotation graph/associahedron graph for
binary trees of size n. Each node in this graph represents a unique
binary tree, and an edge exists between two nodes if one tree can be
transformed into the other via a single rotation operation. The graph will
be stored as a networkx graph object for analysis and visualization.
"""

import sys

sys.path.append('..')

from structs.binaryTree import BinaryTree
from structs.polygon import TriangulatedPolygon
import generate_all_rotations as gar

from itertools import combinations
import networkx as nx

def generate_rotation_graph(n: int) -> nx.Graph:
    """
    Generates the rotation graph for binary trees of size n.
    
    :param n: Number of nodes in the binary trees.
    :return: A networkx Graph object representing the rotation graph.
    """
    all_trees, adjacency = gar.generate_all_rotations(n)
    G = nx.Graph()

    # Add nodes to the graph
    for tree in all_trees:
        preorder = str(tree.preorder_traversal())
        G.add_node(preorder, tree=tree)

    # Add edges based on adjacency
    for tree_preorder, neighbors in adjacency.items():
        for neighbor in neighbors:
            G.add_edge(tree_preorder, neighbor)

    return G
    