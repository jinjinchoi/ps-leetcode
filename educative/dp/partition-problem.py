def can_partition(set):
    sorted_list = sorted(set, reverse=True)
    print(sorted_list)
    sum_set = sum(set)
    if sum_set %2 != 0:
        return False
    
    target = sum_set //2
    print("target:{}".format(target))
    

    def recursion(lookup_table, remaining, index, set):
        print("recursion called for remaining {} index {}".format(remaining, index))
        if lookup_table[index][remaining] != -1:
            print("exists in lookup_table")
            return lookup_table[index][remaining]
        if index>=len(set) or remaining<0:
            lookup_table[index][remaining]=False
            return False
        if remaining in set[index:]:
            lookup_table[index][remaining] = True
            return True
        
        result1 = recursion(lookup_table, remaining - set[index], index+1, set)
        lookup_table[index+1][remaining - set[index]] = result1
        result2 = recursion(lookup_table, remaining, index+1, set)
        lookup_table[index+1][remaining] = result2
        return result1 or result2

    
    lookup_table = [[-1 for x in range(sum_set)] for x in range(len(set)+1) ]
    return recursion(lookup_table, target, 0, sorted_list)
    
    
print(can_partition([2,2,2,2,2,2,2,4,8]))
