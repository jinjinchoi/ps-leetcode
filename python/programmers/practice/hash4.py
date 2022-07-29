from collections import defaultdict

def solution(clothes):
    answer = 1
    clothe_dict = defaultdict(int)
    for v, k in clothes:
        clothe_dict[k] += 1
        
    for k,v in clothe_dict.items():
        answer *= (v+1)
    return answer-1
