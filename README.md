# Data Structures and Algorithms II - Tree Traversal

This is the starter code for Computer Science - Sprint 3: Data Structures and Algorithms II - Tree Traversal.

Please fork and clone this repo to your computer by the start of class.


# binary tree traversal code in python

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
    
def traverse_tree(root):
    print(root.data)

    if root.left:
        traverse_tree(root.left)
    if root.right:
        traverse_tree(root.right)

root = Node(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)

traverse_tree(root)
