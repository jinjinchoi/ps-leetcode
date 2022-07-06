from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    # create hash
    # pyramid_dict = defaultdict(list)
    refer_dict = {}
    revenue_dict = dict.fromkeys(set(enroll),0)
    # print(revenue_dict)
    for r, e in zip(referral, enroll):
        # pyramid_dict[r].append(e)
        refer_dict[e] = r
        
    for a, s in zip(amount, seller):
        revenue = 100*a
        e = s
        while e != '-' and revenue>0:
            revenue_dict[e] += (revenue - revenue//10)
            e = refer_dict[e]
            revenue = revenue//10
        
    # print(pyramid_dict)
    # print(revenue_dict)

    return [revenue_dict[e] for e in enroll]
