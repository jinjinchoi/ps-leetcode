from collections import deque

def solution(n, computers):
    global answer
    answer = 0
    visited = [False] * len(computers)
    
    def bfs(v):
        global answer
        graph = deque()
        graph.append(v)
        visited[v] = True
        while graph:
            index = graph.popleft()
            for i, adjacent in enumerate(computers[index]):
                if i!=index and adjacent==1 and not visited[i]:
                    graph.append(i)
                    visited[i] = True
        answer += 1
        return
        
    while False in visited:
        bfs(visited.index(False))
        
    return answer
