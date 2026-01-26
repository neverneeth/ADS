"""
Docstring for BTR.map_rotations
This module aims to create the rotation graph/associahedron graph for
binary trees of size n. Each node in this graph represents a unique
binary tree, and an edge exists between two nodes if one tree can be
transformed into the other via a single rotation operation. The graph will
be stored as a networkx graph object for analysis and visualization.
"""

from src.structs.binaryTree import BinaryTree
from src.structs.polygon import TriangulatedPolygon
from src.BTR import generate_all_rotations as gar

from itertools import combinations
import networkx as nx
import iplotx as ipx
import matplotlib
import matplotlib.pyplot as plt

def generate_rotation_graph(n: int) -> nx.Graph:
    """
    Generates the rotation graph for binary trees of size n.
    
    :param n: Number of nodes in the binary trees.
    :return: A networkx Graph object representing the rotation graph.
    """
    all_trees, adjacency = gar.generate_all_rotations(n)
    G = nx.Graph(adjacency)
    return G

if __name__ == "__main__":
    n = 5  # Example size
    fig, ax = plt.subplots(figsize=(n*3, n*3))
    rotation_graph = generate_rotation_graph(n)
    layout = nx.layout.spring_layout(rotation_graph)
    print(f"Generated rotation graph with {rotation_graph.number_of_nodes()} nodes and {rotation_graph.number_of_edges()} edges.")
    nx.draw(rotation_graph, pos=layout, with_labels=True, node_size=500, ax=ax)
    if True:
        matplotlib.use('Agg')
        fig.savefig("rotation_graph.png")
