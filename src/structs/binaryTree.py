from typing import Optional, Tuple, Any

TreeNode = Optional[Tuple[Any, 'TreeNode', 'TreeNode']]


class BinaryTree:
    def __init__(self, tree: TreeNode = None):
        self.tree = tree

    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return (value, None, None)
            root, left, right = node
            if value < root:
                left = _insert(left, value)
            else:
                right = _insert(right, value)
            return (root, left, right)
        
        self.tree = _insert(self.tree, value)

    def generate_right_skewed_tree(self, n):
        """
        Docstring for generate_right_skewed_tree
        
        :param n: Size of the tree, defined as the number of (internal) nodes.
        :return: A right-skewed binary tree with n nodes.
        """
        for i in range(1, n+1):
            self.insert(i)
    
    def inorder_traversal(self):
        def _inorder(node):
            if node is None:
                return []
            root, left, right = node
            return _inorder(left) + [root] + _inorder(right)
        
        return _inorder(self.tree)

    def preorder_traversal(self):
        def _preorder(node):
            if node is None:
                return []
            root, left, right = node
            return [root] + _preorder(left) + _preorder(right)
        
        return _preorder(self.tree)

    @staticmethod
    def from_tuple(tree_tuple: TreeNode) -> 'BinaryTree':
        bt = BinaryTree()
        bt.tree = tree_tuple
        return bt
    
    def to_tuple(self) -> TreeNode:
        return self.tree
    
    def get_height(self):
        def _get_height(node):
            if not node:
                return 0
            root, left, right = node
            return 1 + max(_get_height(left), _get_height(right))
        return _get_height(self.tree)
    
    def get_size(self) -> int:
        tup = self.to_tuple()
        if tup is None:
            return 0
        root, left, right = tup
        left_size = BinaryTree.from_tuple(left).get_size()
        right_size = BinaryTree.from_tuple(right).get_size()
        return 1 + left_size + right_size
        
    
    def _replace_node(self, current: TreeNode, target: TreeNode, new_subtree: TreeNode) -> TreeNode:
        """
        Recursively replace the first occurrence of target node with new_subtree in the tree.
        Returns the new tree with the replacement.
        """
        if current is None:
            return None
        if current is target:
            return new_subtree
        root, left, right = current
        return (root, self._replace_node(left, target, new_subtree), self._replace_node(right, target, new_subtree))

    def rotate_right(self, node: TreeNode):
        """
        Rotates right at the given node and updates the tree instance in-place.
        """
        if not node or not node[1]:
            return
        root, left, right = node
        if left is None:
            return
        left_root, left_left, left_right = left
        new_root = (left_root, left_left, (root, left_right, right))
        self.tree = self._replace_node(self.tree, node, new_root)

    def rotate_left(self, node: TreeNode):
        """
        Rotates left at the given node and updates the tree instance in-place.
        """
        if not node or not node[2]:
            return
        root, left, right = node
        if right is None:
            return
        right_root, right_left, right_right = right
        new_root = (right_root, (root, left, right_left), right_right)
        self.tree = self._replace_node(self.tree, node, new_root)