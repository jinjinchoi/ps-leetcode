from collections import defaultdict
def solution(participant, completion):
    answer = ''
    
    marathon_dict = defaultdict(int)
    for p in participant:
        marathon_dict[p] += 1
        
    for c in completion:
        marathon_dict[c] -= 1
        if marathon_dict[c] == 0:
            del marathon_dict[c]
        
    k, v = marathon_dict.popitem()
    return k
