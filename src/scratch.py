class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        # first node is data. if self.data is None, then it is the first node
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            # otherwise, keep going left
            else:
                self.left.insert(data)
        # if data is greater than self.data, then go right
        else:
            # if self.right is None, then it is the first node
            if self.right is None:
                self.right = Node(data)
            # otherwise, keep going right
            else:
                self.right.insert(data)
    
 # can print a tree of size n
 # preorder traversal   
 # depth first traversal
def traverse_tree(root):
    print(root.data)

    if root.left:
        traverse_tree(root.left)
    if root.right:
        traverse_tree(root.right)

# in order traversal
def traverse_tree2(root):
    if root.left:
        traverse_tree2(root.left)
    print(root.data)

    if root.right:
        traverse_tree2(root.right)

# post order traversal
def traverse_tree3(root):
    if root.left:
        traverse_tree3(root.left)
    if root.right:
        traverse_tree3(root.right)
    print(root.data)

root = Node(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(1)
root.insert(3)
root.insert(12)
root.insert(11)
root.insert(13)


traverse_tree(root)
# traverse_tree2(root)
# traverse_tree3(root)