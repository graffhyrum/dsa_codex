# A binary search tree

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()
