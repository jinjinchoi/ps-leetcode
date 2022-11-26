def sliding_window_max(nums, k):
    from collections import deque

    q = deque() # stores *indices*
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()
        q.append(i)
        # remove first element if it's outside the window
        if q[0] == i - k:
            q.popleft()
        # if the window has k elements, add to results
        # (first k-1 windows have < k elements because 
        # we start from empty window and add 1 element each iteration)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res

#Driver code
inputs = ['3','2','3']
inputs1 = ['1 3 2 5 8 7','1 2 3 4 5 6 7 8','1 3 1 2 0 5']
for i in range(len(inputs)):
    arr = [int(x) for x in inputs1[i].split()]
    k = int(inputs[i])
    print("Sliding window max :",sliding_window_max(arr, k))
