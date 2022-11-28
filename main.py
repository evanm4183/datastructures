# File for testing any of the classes

from binarytree.tree import Tree
from binarytree.TreeNode import TreeNode

simple_tree = Tree([20, 10, 30, 40, 5, 25, 35, 45, 15, 33])
simple_tree.insert_node(1)

simple_tree.all_orders()

simple_tree.delete_node(10)

simple_tree.all_orders()
