from typing import Dict, List
class Node:
    def __init__(self, val):
        self.val = val   
def get_length_of_shortest_path(graph: Dict[Node, List[Node]], A: Node, B: Node) -> int:
    def get_neighbors(node):
        return graph[node]

    from collections import deque

    def bfs(root, target):
        queue = deque([root])
        visited = set()
        level = 0
        while len(queue) > 0:
            n = len(queue) # get # of nodes in the current level
            for n in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level += 1
    return bfs(A, B)

# Driver code
# of edges, edges, start node, end node
input1 = [[[1,2],[0,2,3],[0,1],[1]], 0, 3]
input2 = [[[1],[0,2],[1,3],[2]], 0, 3]

for data in [input1, input2]:
    n = len(data[0])
    nodes = { i:  Node(i) for i in range(n) }
    graph = { }
    for k in range(n):
        graph[nodes[k]] = [nodes[i] for i in data[0][k]]
    A = nodes[data[1]]
    B = nodes[data[2]]
    print("Length of shortest path : ",get_length_of_shortest_path(graph, A, B))
