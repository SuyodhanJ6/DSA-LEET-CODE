
import queue




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(root):
    if root is None:
        return
    print(root.data)
    pre_order(root.left)
    pre_order(root.right)


def maxDepth_BFS(root):
    if not root:
        return 0

    # level = 0
    # q = deque([root])
    # while 1:

        # for _ in range(len(q)):
        #     node = q[0]
        #     q.popleft()
        #     if node.left:
        #         q.append(root.left)
        #     if node.right:
        #         q.append(root.right)
        # level += 1
    # print("level is ", level)
    
    
    queue = [root]
    maxWidth = 0
    while 1:
        start = False
        end = False
        pos = 1
        for i in range(len(queue)):
            currentNode = queue[0]
            queue.pop(0)

            if currentNode is not None:
                if not start:
                    start = pos
                else:
                    end = pos
                
                queue.append(currentNode.left)
                queue.append(currentNode.right)
            else:
                queue.append(None)
                queue.append(None)
            
            pos + 1
        
        if start == False and end == False:
            break
        else:
            if start and end:
                maxWidth = max(maxWidth, (end - start) + 1)

    return maxWidth


    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)
root.right.left.right = Node(7)
# pre_order(root)

maxDepth_BFS(root)