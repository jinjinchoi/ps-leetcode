def solution(numbers):
    answer = []
    
    for n in numbers:
        if last_consecutive_ones(n)>3:
            r = n + 1 + int('1'*(last_consecutive_ones(n)-1), 2)
        else:
            r = n+1
            while not has_small_diff(n, r):
                r += 1
        answer.append(r)
    return answer


def has_small_diff(num1, num2):
    xor_value = bin(num1 ^ num2)
    return xor_value.count("1") < 3


def last_consecutive_ones(num):
    binary_rep = bin(num)
    count = 0
    while binary_rep[-1] == '1':
        binary_rep = binary_rep[:-1]
        # print(binary_rep)
        count += 1
    # print(count)
    return count
