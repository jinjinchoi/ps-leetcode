import itertools
def solution(k, dungeons):
    answer = -1
    
    
    permutations = list(itertools.permutations(range(0, len(dungeons))))
    # sorted(dungeons, key = lambda x: x[1])

    index = 0
    curr = k
    count = 0
    count_list = []
    for index_list in permutations:
        # print(index_list)
        curr = k
        count = 0
        for i in index_list:
            min_pow, consume_pow = dungeons[i]
            if curr >= min_pow:
                curr -= consume_pow
                count += 1
                # print("current {} - consume_pow: {} = {}".format(curr+consume_pow, consume_pow, curr))
        count_list.append(count)
    
    
    return max(count_list)


# 어려운건 못풀고..brute force는 잘 풀릴 때의 이 현타란.....
