from collections import deque
def solution(s):
    stack = deque()
    for p in s:
        if len(stack)==0 and p==')':
            return False
        elif len(stack)==1 and stack[-1]==')':
            return False
        elif p==')' and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(p)

    return False if stack else True
