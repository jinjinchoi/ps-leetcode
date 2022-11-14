from collections import deque

def binary_tree_min_depth(root):
	queue = dequeue([root])
	
	level = -1
	while len(queue)>0:
		n = len(queue)
		level += 1	
		for _ in range(n):
			node = queue.popleft()
			if node.left is None and node.right is None:
				return level
			for child in [node.left, node.right]:
				if child is not None:
					queue.append(child)
	return level

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
    print("Binary tree min depth : ",binary_tree_min_depth(root))
