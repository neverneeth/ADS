"""Binary Search Tree (BST) as nested tuples in Python.
Includes insertion, deletion, search, and traversal methods."""

class BinaryTree:
    def __init__(self):
        self.tree: tuple = ()
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return (value, (), ())
            root, left, right = node
            if value < root:
                return (root, _insert(left, value), right)
            elif value > root:
                return (root, left, _insert(right, value))
            return node
        self.tree = _insert(self.tree, value)
    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            root, left, right = node
            if value == root:
                return True
            elif value < root:
                return _search(left, value)
            else:
                return _search(right, value)
        return _search(self.tree, value)
    def delete(self, value):
        def _delete(node, value):
            if not node:
                return node
            root, left, right = node
            if value < root:
                return (root, _delete(left, value), right)
            elif value > root:
                return (root, left, _delete(right, value))
            else:
                # Node with only one child or no child
                if not left:
                    return right
                elif not right:
                    return left
                # Node with two children: Get the inorder successor (smallest in the right subtree)
                succ_value = self._min_value(right)
                return (succ_value, left, _delete(right, succ_value))
        self.tree = _delete(self.tree, value)
    def _min_value(self, node):
        current = node
        while current and current[1]:  # Traverse to the leftmost node
            current = current[1]
        return current[0] if current else None
    def inorder_traversal(self):
        def _inorder(node):
            if not node:
                return []
            root, left, right = node
            return _inorder(left) + [root] + _inorder(right)
        return _inorder(self.tree)
    def preorder_traversal(self):
        def _preorder(node):
            if not node:
                return []
            root, left, right = node
            return [root] + _preorder(left) + _preorder(right)
        return _preorder(self.tree)
    def postorder_traversal(self):
        def _postorder(node):
            if not node:
                return []
            root, left, right = node
            return _postorder(left) + _postorder(right) + [root]
        return _postorder(self.tree)