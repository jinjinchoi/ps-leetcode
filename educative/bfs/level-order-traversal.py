from collections import deque
from typing import List


def level_order_traversal(root):
    res = []
    queue = deque([root])  # at least one element in the queue to kick start bfs
    print("start with root: {}".format(root.val))
    while len(queue) > 0:  # as long as there is element in the queue
        n = len(queue)  # number of nodes in current level, see explanation above
        new_level = []
        print("current level n: {}".format(n))
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            print("node popped: {}".format(node.val))
            new_level.append(node)
            for child in [node.left, node.right]:  # enqueue non-null children
                if child is not None:
                    queue.append(child)
                    print("child appended: {}".format(child.val))
        res.append(new_level)
        print("new_level appended: {}".format(list(map(lambda x: x.val, new_level))))
    return res


# Driver code
class Node:

    def __init__(
        self,
        val,
        left=None,
        right=None,
        ):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes):
    val = next(nodes)
    if not val or val == 'x':
        return
    cur = Node(int(val))
    cur.left = build_tree(nodes)
    cur.right = build_tree(nodes)
    return cur


inputs = ['1 2 4 x 7 x x 5 x x 3 x 6 x x', '0 x x']
for i in range(len(inputs)):
    root = build_tree(iter(inputs[i].split()))
    actual_output = []
    node_output = level_order_traversal(root)
    for level in node_output:
        output = []
        for x in level:
            output.append(x.val)
        actual_output.append(output)
    print ('Level order traversal :', actual_output)
