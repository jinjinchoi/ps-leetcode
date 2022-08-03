def solution(sizes):
    answer = 0
    
    horizontal = []
    vertical = []
    for x, y in sizes:
        horizontal.append(max(x,y))
        vertical.append(min(x,y))
    return max(horizontal) * max(vertical)
