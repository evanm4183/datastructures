from binarytree.leaf import Leaf

# binary search tree for numbers
class Tree:
    def __init__(self, val):
        self.root = Leaf(val)

    # method for inserting a number into the tree
    def insert(self, val):
        def insert_leaf(curr_leaf, val):
            if val == curr_leaf.val:
                return
            elif val < curr_leaf.val and curr_leaf.left is None:
                curr_leaf.left = Leaf(val)
            elif val > curr_leaf.val and curr_leaf.right is None:
                curr_leaf.right = Leaf(val)
            elif val < curr_leaf.val:
                insert_leaf(curr_leaf.left, val)
            elif val > curr_leaf.val:
                insert_leaf(curr_leaf.right, val)

        insert_leaf(self.root, val)

    # method for inserting a list of numbers into the tree
    def insert_list(self, list):
        for num in list:
            self.insert(num)

    # returns a list with the preorder traversal of the tree
    def preorder(self):
        def get_preorder(leaf, vals):
            if leaf is not None:
                vals.append(leaf.val)
                get_preorder(leaf.left, vals)
                get_preorder(leaf.right, vals)

            return vals

        return get_preorder(self.root, [])

    # returns a list with the inorder traversal of the tree
    def inorder(self):
        def get_inorder(leaf, vals):
            if leaf is not None:
                get_inorder(leaf.left, vals)
                vals.append(leaf.val)
                get_inorder(leaf.right, vals)

            return vals

        return get_inorder(self.root, [])

    # returns a list with the postorder traversal of the tree
    def postorder(self):
        def get_postorder(leaf, vals):
            if leaf is not None:
                get_postorder(leaf.left, vals)
                get_postorder(leaf.right, vals)
                vals.append(leaf.val)

            return vals

        return get_postorder(self.root, [])

            
            






