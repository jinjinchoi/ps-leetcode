from typing import List
def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    l, r = 0, len(arr) - 1
    while l < r:
        two_sum = arr[l] + arr[r]
        if two_sum == target:
            return [l, r]
        if two_sum < target:
            l += 1
        else:
            r -= 1

#Drive code
inputs = ["2 3 4 5 8 11 18","2 5 10 12 30 100","1 2 3 10 20 30 50 100","1 2", "100 1000 2001 3000 4000 5000"]
inputs1 = ["8","22","101","3","5001"]
for i in range(len(inputs)):
    arr = [int(x) for x in inputs[i].split()]
    target = int(inputs1[i])
    res = two_sum_sorted(arr, target)
    print("Two sim sorted",' '.join(str(e) for e in res))
