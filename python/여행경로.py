from collections import defaultdict

def solution(tickets):
    answer = []
    # create hashmap
    ticket_dict = defaultdict(list)
    for _from, _to in tickets:
        ticket_dict[_from].append(_to)
    for k in ticket_dict.keys():
        ticket_dict[k].sort()
    # iterate through hashmap
    _from = 'ICN'
    route = ['ICN']
    visited = []
    # while 탈출 조건 : 항공권을 모두 사용했을 때
    while route:
        if ticket_dict[route[-1]]:
            _to = ticket_dict[route[-1]].pop(0)
            route.append(_to)
        else:
            # 막다른 곳 -> 마지막 종착지!
            answer.append(route.pop())
    return answer[::-1]
