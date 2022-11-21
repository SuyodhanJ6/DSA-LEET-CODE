
from collections import deque

import queue




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def maxDepth(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    level = 1
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        level +=1
    return level


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)
# pre_order(root)

maxDepth(root)