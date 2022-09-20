def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    h_index = citations[n-1]+1
    condition = False
    # 0 1 2 2 2 3
    while condition!= True:
        h_index -= 1
        num_over_h = count_num_over_h(h_index, citations)
        num_under_h = n - num_over_h
        condition = (num_under_h<=h_index) and (num_over_h >= h_index)
        # if num_under_h > h_index:
        #     index = citations.index(h_index) - 1
        # elif num_over_h < h_index:
        #     index = citations.index(h_index) - 1
        #     # else:
        #     #     break
        # else:
        #     break

    return h_index

def count_num_over_h(h, num_list): 
    reverse_num = reversed(sorted(num_list))
    counter = 0
    for n in reverse_num:
        if n >= h:
            counter += 1
        else:
            break
    return counter
