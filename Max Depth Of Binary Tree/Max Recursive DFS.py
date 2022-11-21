
class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth_DFS(root):
    if not root:
        return 0
    return 1+ max(max_depth_DFS(root.left), max_depth_DFS(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)

print("the maximum depth of tree is: ", max_depth_DFS(root))

