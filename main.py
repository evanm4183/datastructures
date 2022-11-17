from binarytree.tree import Tree
from binarytree.leaf import Leaf

new_tree = Tree(10)
new_tree.root.display_leaf()

new_tree.insert_list([5, 15])
new_tree.root.display_leaf()