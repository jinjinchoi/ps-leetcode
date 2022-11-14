from collections import deque

def zigzag_traversal(root):
    res = []
    queue = deque([root])  # at least one element in the queue to kick start bfs
    left_to_right = True
    while len(queue) > 0:  # as long as there is element in the queue
        n = len(queue)  # number of nodes in current level, see explanation above
        new_level = []
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            new_level.append(node)
            for child in [node.left, node.right]:  # enqueue non-null children
                if child is not None:
                    queue.append(child)
        if not left_to_right:
            new_level.reverse()  # reverse current level
        res.append(new_level)
        left_to_right = not left_to_right  # flip flag
    return res

#Driver code
class Node:
      def __init__(self, val, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
  
def build_tree(nodes):
      val = next(nodes)
      if not val or val == 'x': return
      cur = Node(int(val))
      cur.left = build_tree(nodes)
      cur.right = build_tree(nodes)
      return cur

inputs = ["1 2 4 x 7 x x 5 x 8 x x 3 x 6 x x"]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    actual_output = []
    node_output = zigzag_traversal(root)
    for level in node_output:
            output = []
            for x in level:
                output.append(x.val)
            actual_output.append(output)
    print("Binary tree zigzag level order traversal : ", actual_output)
