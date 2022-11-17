from collections import defaultdict
from enum import Enum

class State(Enum):
    TO_VISIT = 0
    VISITING = 1
    VISITED = 2

def is_valid_course_schedule(n, prerequisites):
    def build_graph():
        graph = defaultdict(list)
        for src, dest in prerequisites:
            graph[src].append(dest)
        return graph

    def dfs(start, states):
        # mark self as visiting
        states[start] = State.VISITING

        for next_vertex in graph[start]:
            # ignore visited nodes
            if states[next_vertex] == State.VISITED:
                continue

            # revisiting a visiting node, CYCLE!
            if states[next_vertex] == State.VISITING:
                return False

            # recursively visit neighbours
            # if a neighbour found a cycle, we return False right away
            if not dfs(next_vertex, states):
                return False

        # mark self as visited
        states[start] = State.VISITED

        # if we have gotten this far, our neighbours haven't found any cycle, return True
        return True

    graph = build_graph()
    states = [State.TO_VISIT for _ in range(n)]

    # dfs on each node
    for i in range(n):
        if not dfs(i, states):
            return False

    return True

#Driver code
inputs = ["2","2", "4"]
inputs1 = ["1", "2", "4"]
inputs2 = [["0 1"],["0 1","1 0"],["0 1","1 2","2 3","3 1"]]
for i in range(len(inputs)):
    n = int(inputs[i])
    num_deps = int(inputs1[i])
    deps = [[int(x) for x in inputs2[i][j].split()] for j in range(num_deps)]
    print("Course schedule :", is_valid_course_schedule(n, deps))
