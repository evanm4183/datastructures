from binarytree.leaf import Node

# binary search tree for numbers
class Tree:
    def __init__(self, val):
        self.root = Node(val)

    # method for inserting a number into the tree
    def insert(self, val):
        def insert_node(curr_node, val):
            if val == curr_node.val:
                return
            elif val < curr_node.val and curr_node.left is None:
                curr_node.left = Node(val)
            elif val > curr_node.val and curr_node.right is None:
                curr_node.right = Node(val)
            elif val < curr_node.val:
                insert_node(curr_node.left, val)
            elif val > curr_node.val:
                insert_node(curr_node.right, val)

        insert_node(self.root, val)

    # method for inserting a list of numbers into the tree
    def insert_list(self, list):
        for num in list:
            self.insert(num)

    # deletes the node with the given value from the tree
    def delete_leaf(self, val):
        def search_and_destroy(node, val):
            if node is None:
                return 'Value does not exist within tree'
            elif val == node.val:
                return 'Delete successful'
            elif val < node.val:
                pass
            elif val > node.val:
                pass

    # returns True or False depending on if the value is contained in the tree
    def contains(self, val):
        def compare(node, val):
            if node is None:
                return False
            elif val == node.val:
                return True
            elif val < node.val:
                return compare(node.left, val)
            elif val > node.val:
                return compare(node.right, val)

        return compare(self.root, val)

    # returns a list with the preorder traversal of the tree
    def preorder(self):
        def get_preorder(node, vals):
            if node is not None:
                vals.append(node.val)
                get_preorder(node.left, vals)
                get_preorder(node.right, vals)

            return vals

        return get_preorder(self.root, [])

    # returns a list with the inorder traversal of the tree
    def inorder(self):
        def get_inorder(node, vals):
            if node is not None:
                get_inorder(node.left, vals)
                vals.append(node.val)
                get_inorder(node.right, vals)

            return vals

        return get_inorder(self.root, [])

    # returns a list with the postorder traversal of the tree
    def postorder(self):
        def get_postorder(node, vals):
            if node is not None:
                get_postorder(node.left, vals)
                get_postorder(node.right, vals)
                vals.append(node.val)

            return vals

        return get_postorder(self.root, [])

            
            






