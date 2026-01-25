from src.structs.binaryTree import BinaryTree

class TriangulatedPolygon:
    def __init__(self, size):
        self.size = size
        self.vertices = tuple(range(-1, size - 1))
        self.diagonals = ()

    def from_binary_tree(self, binary_tree: BinaryTree):
        """
        Docstring for from_binary_tree

        In the STT paper, a correspondence between binary trees and triangulated polygons is described.
        
        :param self: Description
        :param binary_tree: Description
        """
        if binary_tree.get_height() + 2 != self.size:
            raise ValueError("Binary tree size must be one less than polygon size.")

        diagonals = []

        def add_diagonal(node, left_index, right_index):
            if node is None:
                return

            mid_index = left_index + (right_index - left_index) // 2
            diagonals.append((self.vertices[left_index], self.vertices[right_index]))

            add_diagonal(node.left, left_index, mid_index)
            add_diagonal(node.right, mid_index, right_index)

        add_diagonal(binary_tree.to_tuple()[0], 0, self.size - 1)
        self.diagonals = tuple(diagonals)
    


