import sys

sys.path.append("..") 

from structs.binaryTree import BinaryTree 

def generate_right_skewed_tree(n) -> BinaryTree:
    """
    Docstring for generate_right_skewed_tree
    
    :param n: Size of the tree, defined as the number of (internal) nodes.
    :return: A right-skewed binary tree with n nodes.
    """
    tree = BinaryTree()
    for i in range(1, n+1):
        tree.insert(i)
    return tree


if __name__ == "__main__":
    n = 5  # Example size
    right_skewed_tree = generate_right_skewed_tree(n)
    print("Inorder Traversal of Right-Skewed Tree:", right_skewed_tree.inorder_traversal())
    print("Preorder Traversal of Right-Skewed Tree:", right_skewed_tree.preorder_traversal())
    print(right_skewed_tree.tree)  
