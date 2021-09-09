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

def breadthFirstTraversal(root, target):
    # create an empty queue
    queue = []
    # add the root to the queue
    queue.append(root)
    # while the queue is not empty
    while len(queue) > 0:
        # remove the first node in the queue
        node = queue.pop(0)
        print(node.data)
        # if the node is the target, return True
        if node.data == target:
            return True
        # otherwise, add the left and right nodes to the queue
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    # if the target is not found, return False
    return False

root = Node(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)

breadthFirstTraversal(root, 7)