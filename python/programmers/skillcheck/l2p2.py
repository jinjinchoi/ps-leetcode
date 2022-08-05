from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = deque([0]*bridge_length)
    
    bridge_queue.popleft()
    bridge_queue.append(truck_weights.pop(0))
    
    count = 1
    sum_bridge = bridge_queue[-1]
    while sum_bridge > 0:
        # move left
        # print(bridge_queue)
        done = bridge_queue.popleft()
        sum_bridge -= done
        
        count += 1
        # push or wait
        if not truck_weights:
            bridge_queue.append(0)
        elif sum_bridge + truck_weights[0] <= weight:
            new = truck_weights.pop(0)
            bridge_queue.append(new)
            sum_bridge += new
        else:
            bridge_queue.append(0)
    
    return count
