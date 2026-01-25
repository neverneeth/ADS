import matplotlib.pyplot as plt
from math import cos, sin, pi
import sys

sys.path.append('.')
from binaryTree import BinaryTree, TreeNode


class TriangulatedPolygon:
    def __init__(self, size=0):
        self.size: int = size
        if size is not None:
            self.vertices = tuple(range(-1, size - 1))
        self.diagonals = ()

    def from_binary_tree(self, binary_tree: BinaryTree):
        """
        Docstring for from_binary_tree

        In the STT paper, a correspondence between binary trees and triangulated polygons is described.
        The procedure as explained by a certain Amy Liu on medium can be summarized as follows:
        1. Given a binary tree of n nodes, create a polygon with n+2 vertices.
        2. Fix a root edge, and label the corresponding vertices 0 and -1.
        3. Label the remaining vertices in counter-clockwise order from 1 to n.
        4. Identify the root node of the binary tree and draw diagonals from 0 and -1 to the corresponding vertex.
        5. Recursively, treating each new diagonal as a root edge, for left and right subtrees, repeat 4.         
        :param self: Description
        :param binary_tree: Description
        """
        self.size = binary_tree.get_size() + 2 
        if binary_tree.get_height() + 2 != self.size:
            raise ValueError("Binary tree size must be one less than polygon size.")
        self.vertices = tuple(range(-1, self.size - 1))
        self.diagonals = self._extract_diagonals(binary_tree.to_tuple(), 0, -1)
        return self
    
    def _extract_diagonals(self, node: TreeNode, v1: int, v2: int):
        if node is None:
            return ()
        root, left, right = node
        diagonals = ((v1, root), (v2, root))
        diagonals += self._extract_diagonals(left, v1, root)
        diagonals += self._extract_diagonals(right, v2, root)
        return diagonals
    
    def plot(self):
        n = self.size
        angles = [2 * pi * i / n for i in range(n)]
        points = [(cos(angle), sin(angle)) for angle in angles]
        fig, ax = plt.subplots()
        polygon_points = points + [points[0]]
        xs, ys = zip(*polygon_points)
        # Label vertices
        for i, (x, y) in enumerate(points):
            ax.text(x, y, str(self.vertices[i]), fontsize=12, ha='right', va='bottom')
        # Draw polygon edges
        ax.plot(xs, ys, 'b-')
        # Draw diagonals
        for diag in self.diagonals:
            v1, v2 = diag
            x_values = [points[v1][0], points[v2][0]]
            y_values = [points[v1][1], points[v2][1]]
            ax.plot(x_values, y_values, 'r--')
        ax.set_aspect('equal')
        plt.savefig("triangulated_polygon.png")
        return fig, ax


if __name__ == "__main__":
    bt = BinaryTree()
    bt.generate_right_skewed_tree(5)
    polygon = TriangulatedPolygon().from_binary_tree(bt)
    print(f"Vertices: {polygon.vertices}")
    print(f"Diagonals: {polygon.diagonals}")