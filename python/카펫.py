def solution(brown, yellow):
    answer = []
    for h in range(1, yellow+1):
        w = yellow//h
        if(w*h != yellow or w<h):
            continue
        if(brown == 2*w+2*h+4):
            return [w+2, h+2]
    return answer
