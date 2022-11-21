class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data)
    in_order(root.right)

def minDepth(root):
    if root is None:
        return 0
    
    return 1+min(minDepth(root.left), minDepth(root.right))
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)


print(f'the minimum depth of BT', minDepth(root))

in_order(root)