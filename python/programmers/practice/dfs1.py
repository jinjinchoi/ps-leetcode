from collections import deque

def solution(numbers, target):
    global answer 
    answer = 0

    def dfs(current_index, current_sum):
        global answer
        # print("current_index: {}, current_sum: {}".format(current_index, current_sum))
        if current_index == len(numbers):
            if current_sum == target:
                answer += 1
                return
            else:
                return
        else:
            dfs(current_index+1, current_sum + numbers[current_index])
            dfs(current_index+1, current_sum - numbers[current_index])
    
    
    dfs(0, 0)
    
    return answer

        
