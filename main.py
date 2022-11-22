from binarytree.tree import Tree
from binarytree.leaf import Node

simple_tree = Tree(20)
simple_tree.insert_list([10, 30, 40, 5, 25, 35, 45, 15])

simple_tree.all_orders()

simple_tree.delete_node(10)

simple_tree.all_orders()
