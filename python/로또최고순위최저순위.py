def solution(lottos, win_nums):
    answer = []
    
    uncertain_count = lottos.count(0)
    while 0 in lottos: lottos.remove(0)    
    certain_correct_count = 0 #todo
    certain_wrong_count = 0 #todo
    for l in lottos:
        if l in win_nums:
            win_nums.remove(l)
            certain_correct_count +=1
        else:
            certain_wrong_count += 1
    return [ranking(6-certain_wrong_count), ranking(certain_correct_count)]


def ranking(correct_count):
    return 6 if correct_count<=1 else 7 - correct_count
    
lottos = 	[44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
