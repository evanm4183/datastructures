from binarytree.tree import Tree
from binarytree.leaf import Leaf

new_tree = Tree(10)
new_tree.root.display_leaf()

new_tree.insert(11)
new_tree.root.display_leaf()

new_tree.insert(9)
new_tree.root.display_leaf()

new_tree.insert(15)
new_tree.root.right.display_leaf()