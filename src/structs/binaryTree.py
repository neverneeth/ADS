class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

class BinaryTree:
    def __init__(self):
        self.root: BSTNode | None = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: BSTNode | None, value) -> BSTNode:
        if current is None:
            return BSTNode(value)
        
        if value < current.value:
            current.left = self._insert_recursive(current.left, value)
        else:
            current.right = self._insert_recursive(current.right, value)
        return current

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current: BSTNode | None, value) -> BSTNode | None:
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            temp = self._get_min_value_node(current.right)
            current.value = temp.value
            current.right = self._delete_recursive(current.right, temp.value)
            
        return current

    def _get_min_value_node(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, value) -> bool:
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current: BSTNode | None, value) -> bool:
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)
            