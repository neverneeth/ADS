import sys

from generate_tree import generate_right_skewed_tree

sys.path.append("..")

from structs.binaryTree import BinaryTree

def rotate_right(node):
    """
    Docstring for rotate_right
    Performs a right rotation on the given binary tree node. 
    
    :param node: A tuple representing the binary tree node to be rotated (root, left, right).
    :return: A new tuple representing the root of the rotated subtree.
    """
    if not node or not node[1]:
        return node # A node requires a left child to perform a right rotation.
    
    root, left, right = node
    left_root, left_left, left_right = left
    new_root = left_root
    new_left = left_left
    new_right = (root, left_right, right)
    return (new_root, new_left, new_right)

def rotate_left(node):
    """
    Docstring for rotate_left
    Performs a left rotation on the given binary tree node. 
    
    :param node: A tuple representing the binary tree node to be rotated (root, left, right).
    :return: A new tuple representing the root of the rotated subtree.
    """
    if not node or not node[2]:
        return node # A node requires a right child to perform a left rotation.
    
    root, left, right = node
    right_root, right_left, right_right = right
    new_root = right_root
    new_left = (root, left, right_left)
    new_right = right_right
    return (new_root, new_left, new_right)


if __name__ == "__main__":
    tree_node: tuple = generate_right_skewed_tree(3).tree
    
    print("Original Node:", tree_node)
    
    rotated_subtree = rotate_right(tree_node[2])
    rotated_right = (tree_node[0], tree_node[1], rotated_subtree)

    print("After Right Rotation:", rotated_right)
    
    rotated_subtree = rotate_left(tree_node[2])
    rotated_left = (tree_node[0], tree_node[1], rotated_subtree)   
    print("After Left Rotation:", rotated_left)


