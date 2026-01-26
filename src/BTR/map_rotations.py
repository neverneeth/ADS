"""
Docstring for BTR.map_rotations
This module aims to create the rotation graph/associahedron graph for
binary trees of size n. Each node in this graph represents a unique
binary tree, and an edge exists between two nodes if one tree can be
transformed into the other via a single rotation operation. The graph will
be stored as a networkx graph object for analysis and visualization.
"""

import os
from src.structs.binaryTree import BinaryTree
from src.structs.polygon import TriangulatedPolygon
from src.BTR import generate_all_rotations as gar

from itertools import combinations
import networkx as nx
import iplotx as ipx
import matplotlib
import matplotlib.pyplot as plt

class AssociahedronGraph:
    """
    Class to represent the associahedron graph of binary trees of size n.
    Each node represents a unique binary tree, and edges represent single
    rotation operations between trees.
    """
    def __init__(self, n: int):
        """
        Initializes the AssociahedronGraph with binary trees of size n.
        
        :param n: Number of nodes in the binary trees.
        """
        self.n = n
        self.trees, self.adjacency = gar.generate_all_rotations(n)
        self.graph = self.generate_rotation_graph(n)

    def generate_rotation_graph(self, n: int) -> nx.Graph:
        """
        Generates the rotation graph for binary trees of size n.
        
        :param n: Number of nodes in the binary trees.
        :return: A networkx Graph object representing the rotation graph.
        """
        all_trees, adjacency = gar.generate_all_rotations(n)
        G = nx.Graph(adjacency)
        return G
    
    def visualize(self, path = None):
        """
        Visualizes the rotation graph using matplotlib and custom logic
        """

        graph = self.graph
        layout = nx.layout.spring_layout(graph)
        nx.draw(graph, pos=layout, with_labels=True, node_size=200)
        if path:
            plt.savefig(f"{path}/rotation_graph_n{self.n}.png")

    def count(self):
        """
        Counts the number of nodes and edges in the rotation graph.
        
        :return: A tuple (number_of_nodes, number_of_edges).
        """
        return self.graph.number_of_nodes(), self.graph.number_of_edges()



if __name__ == "__main__":
    n = 5  # Example size
    fig, ax = plt.subplots(figsize=(n*3, n*3))
    associahedron_graph = AssociahedronGraph(n)
    
    print(f"Generated rotation graph with {associahedron_graph.count()[0]} nodes and {associahedron_graph.count()[1]} edges.")
    if (os.path.exists("./results")) == False:
        os.mkdir("./results")
    associahedron_graph.visualize("./results")
