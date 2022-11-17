class Leaf:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def display_leaf(self):
        print(f'Self: {self.val}')

        if (self.left is not None):
            print(f'Left: {self.left.val}')
        else:
            print(f'Left: {self.left}')

        if (self.right is not None):
            print(f'Left: {self.right.val}')
        else:
            print(f'Right: {self.right}')
        
        print('-------------------')