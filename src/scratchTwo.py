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
# post order traversal recursive
def traverse_tree_post_order(node):
    if node.left: 
        traverse_tree_post_order(node.left)
    if node.right:
        traverse_tree_post_order(node.right)
    print(node.data)


# in order traversal recursive
def traverse_iterative(root, target):
    # setup phase
    stack = []
    stack.append(root)
    # loop phase
    while len(stack) > 0:
        # process phase
        # process the top of the stack
        current_node = stack.pop()
        print(current_node.data)

        if current_node.data == target:
            return True

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return False


def search_recursive(root, target):  

    if root.data == target:
        return True
    if not root.left and not root.right:
        return False
    
    is_found_in_left = False
    is_found_in_right = False
    
    if root.left:
        is_found_in_left = search_recursive(root.left, target)
    if root.right:
        is_found_in_right = search_recursive(root.right, target)
  
    return is_found_in_left or is_found_in_right
    

root = Node(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)
# traverse_tree(root)
# traverse_tree2(root)
# traverse_iterative(root, 5)     
print(search_recursive(root, 5))
        