"""
Docstring for generate_all_rotations

Two trees, T1 and T2 are said to be rotationally equivalent if
one can be transformed into the other by a series of rotations, ie. 
They are trees with the same inorder traversal. This script, for a
given n generates first the right skewed tree with n nodes and then
applies all possible rotations to generate all rotationally equivalent
trees. 

Present intuition is to use BFS to explore all possible rotations
at each node level by level.
"""

import sys

sys.path.append("./")
from src.structs.binaryTree import BinaryTree
from collections import deque

def generate_all_rotations(n):
    """
    Docstring for generate_all_rotations
    Generates all rotationally equivalent binary trees for a right-skewed tree with n nodes.
    
    :param n: Number of nodes in the right-skewed binary tree.
    :return: A list of BinaryTree instances representing all rotationally equivalent trees.
    :return: A dictionary representing adjacency list of rotations.
    """
    initial_tree = BinaryTree()
    initial_tree.generate_right_skewed_tree(n)
    unique_trees = set()
    result_trees = []

    queue = deque([initial_tree])
    adjacency = {}
    while queue:
        current_tree = queue.popleft()
        tree_tuple = current_tree.to_tuple()
        preorder = str(current_tree.preorder_traversal())
        adjacency[preorder] = [] if preorder not in adjacency else adjacency[preorder]
        if tree_tuple not in unique_trees:
            unique_trees.add(tree_tuple)
            result_trees.append(current_tree)

            nodes_to_rotate = []

            def collect_nodes(node):
                if node is None:
                    return
                root, left, right = node
                nodes_to_rotate.append(node)
                collect_nodes(left)
                collect_nodes(right)

            collect_nodes(current_tree.tree)

            for node in nodes_to_rotate:
                new_tree_right = BinaryTree.from_tuple(current_tree.to_tuple())
                new_tree_right.rotate_right(node)
                queue.append(new_tree_right)
                adjacency[preorder].append(str(new_tree_right.preorder_traversal()))

                new_tree_left = BinaryTree.from_tuple(current_tree.to_tuple())
                new_tree_left.rotate_left(node)
                queue.append(new_tree_left)
                adjacency[preorder].append(str(new_tree_left.preorder_traversal()))
    return result_trees, adjacency

if __name__ == "__main__":
    n = 4  # Example size
    all_rotations, adjacency = generate_all_rotations(n)
    print(f"Total unique rotationally equivalent trees for n={n}: {len(all_rotations)}")
    for idx, tree in enumerate(all_rotations):
        print(f"Tree {idx + 1}: {tree.tree}")

    print("Adjacency List:")
    for key, values in adjacency.items():
        print(f"{key}: {values}")