from collections import defaultdict, deque


def solution(tickets):

    airport_graph = defaultdict(list)
    
    stack = ["ICN"]
    
    for _from, _to in tickets:
        airport_graph[_from].append(_to)
        airport_graph[_from].sort(reverse=True)
        
    answer =  []
    while stack:
        v = stack[-1]
        if not airport_graph[v]:
            answer.append(stack.pop())
        else:
            stack.append (airport_graph[v].pop())
                

    return answer[::-1]



