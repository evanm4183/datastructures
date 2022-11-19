from binarytree.tree import Tree
from binarytree.leaf import Leaf

new_tree = Tree(10)
new_tree.insert_list([5, 15, 2, 7, 12, 17, 3, 6, 11, 14])

preorder_list = new_tree.preorder()
print(f'Preorder: {preorder_list}')

inorder_list = new_tree.inorder()
print(f'Inorder: {inorder_list}')

postorder_list = new_tree.postorder()
print(f'Postorder: {postorder_list}')