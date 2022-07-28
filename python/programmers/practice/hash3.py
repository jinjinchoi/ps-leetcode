from collections import defaultdict

def solution(phone_book):
    phone_book.sort()
    
    phone_dict = defaultdict(list)
    for phone_num in phone_book:
        phone_dict[phone_num[0]].append(phone_num)
        
    for k, v in phone_dict.items():
        for i in range(len(v)-1):
            if v[i] in v[i+1]:
                return False
        
        
    return True
