from collections import deque
def solution(arr):
    answer = []
    
    stack = deque([arr[0]])
    for num in arr:
        if num == stack[-1]:
            continue
        else:
            stack.append(num)

    return list(stack)
