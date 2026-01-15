from src.structs.binaryTree import BinaryTree

class TriangulatedPolygon:
    def __init__(self, size):
        self.size = size
        self.vertices = tuple(range(-1, size - 1))
        self.diagonals = ()

    def from_binary_tree(self, binary_tree: BinaryTree):
        """
        Docstring for from_binary_tree
        
        :param self: Description
        :param binary_tree: Description
        """
    


