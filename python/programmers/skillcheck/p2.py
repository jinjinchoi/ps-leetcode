def solution(s):
    answer = 0
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    start_index = 0
    for i, c in enumerate(s):
        num = s[start_index:i+1]
        if num in list(num_dict.keys()):
            answer = concat_num(answer, num_dict[num])
            start_index = i+1
        elif c.isdigit():
            answer = concat_num(answer, c)
            start_index = i+1    
    return int(answer)

def concat_num(num1, num2):
    if num1 == 0:
        return num2
    else:
        return int(str(num1) + str(num2))
