import heapq
def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    for op in operations:
        # INSERT
        if op.startswith('I'):
            heapq.heappush(min_heap, int(op[2:]))
            heapq.heappush(max_heap, (-int(op[2:]), int(op[2:])))
        elif not min_heap:
            pass
        # DELETE MINIMUM
        elif '-' in op:
            _min = heapq.heappop(min_heap)
            # print(_min)
            max_heap.remove((-1*_min, _min))
        # DELETE MAXIMUM
        else:
            _max = heapq.heappop(max_heap)
            min_heap.remove(_max[1])
    if min_heap:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        answer = [0,0]
    return answer
