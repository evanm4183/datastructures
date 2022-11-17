from binarytree.leaf import Leaf

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
