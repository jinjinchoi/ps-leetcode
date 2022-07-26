from collections import defaultdict
def solution(N, number):
    if N == number:
        return 1
    
    digits_dict = defaultdict(set)
    digits_dict[1] = {N}
    def add(num1, num2=N):
        return num1+num2
    def sub(num1, num2=N):
        return max(num1, num2) - min(num1, num2)
    def mul(num1, num2=N):
        return num1 * num2
    def div(num1, num2=N):
        return max(num1, num2) // min(num1, num2)

    for i in range(2, 9):
        for j in range(1, i//2+1):
            for num1 in digits_dict[i-j]:
                for num2 in digits_dict[j]:
                    set_nums = set(filter(lambda x: x>0, [int(str(N)*i), add(num1, num2), sub(num1, num2), mul(num1, num2), div(num1, num2)]))

                    # print("num1: {} / {},  num2: {} / {}".format(num1, digits_dict[i-j], num2, digits_dict[j]))

                    if number in set_nums:
                        return i
                    digits_dict[i].update(set_nums)
            
                # print("updated: {}".format(digits_dict[i]))
        
    
    return -1


