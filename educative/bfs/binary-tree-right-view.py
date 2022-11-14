from collections import deque

def binary_tree_right_side_view(root):
      res = []
      queue = deque([root]) # at least one element in the queue to kick start bfs
      while len(queue) > 0: # as long as there is element in the queue
          n = len(queue) # number of nodes in current level
          res.append(queue[0]) # only append the first node we encounter since it's the rightmost
          for _ in range(n): # dequeue each node in the current level
              node = queue.popleft()
              for child in [node.right, node.left]: # we add right children first so it'll pop out of the queue first
                  if child is not None:
                      queue.append(child)
      return res

# Driver code
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

inputs = ["1 2 4 x 7 x x 5 x x 3 x 6 x x","0 x x"]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    actual_output = ' '.join(str(x.val) for x in binary_tree_right_side_view(root))
    print("Binary tree right slde : ", actual_output)
