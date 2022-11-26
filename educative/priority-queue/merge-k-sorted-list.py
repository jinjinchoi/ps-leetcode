from typing import List

def merge_k_sorted_lists(lists: List[List[int]]) -> List[List[int]]:
    res = []
    import heapq
    heap = []
    for current_list in lists:
        # push first number of each list into the heap
        heapq.heappush(heap, (current_list[0], current_list, 0)) # 1

    while heap:
        val, current_list, head_index = heapq.heappop(heap)
        res.append(val)
        head_index += 1
        # if there are more numbers in the list, push into the heap
        if head_index < len(current_list):
            heapq.heappush(heap, (current_list[head_index], current_list, head_index))

    return res

#Driver code
inputs = ["3","1"]
inputs1 = [["1 3 5","2 4 6","7 10"],["1 2 3"]]
for i in range(len(inputs)):
    n = int(inputs[i])  
    lists = []
    for j in range(n):
        lists.append([int(x) for x in inputs1[i][j].split()])
    res = merge_k_sorted_lists(lists)
    print("Merge k sorted lists :",str(res))
