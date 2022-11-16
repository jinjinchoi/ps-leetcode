def binary_tree_distance_k_nodes(root, target, K):
    from collections import deque

    def find_target(root):
        level = 0
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            level += 1
            for _ in range(n):
                node = queue.popleft()
                if node == target: # early exit if found target
                    return level
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)

    def bfs(root, res):
        level = 0
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            level += 1
            for _ in range(n):
                node = queue.popleft()
                if abs(target_level - level) == K: # found nodes K away from target
                    res.append(node)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
        return res

    res = []
    if root:
        target_level = find_target(root)
        bfs(root, res)
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

def find_node(root, target):
    if not root: return
    if root.val == target: return root
    return find_node(root.left, target) or find_node(root.right, target)

inputs = ["1 2 4 x 7 x x 5 x 8 x x 3 x 6 x x","0 1 x x 2 x x"]
inputs1 = ["6","2"]
inputs2 = ["1","0"]
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    target = find_node(root, int(inputs1[i]))   
    K = int(inputs2[i])
    actual_output = ' '.join(str(x.val) for x in sorted(binary_tree_distance_k_nodes(root, target, K), key=lambda node: node.val))
    print("Binary tree distance K from target node : ", actual_output)
