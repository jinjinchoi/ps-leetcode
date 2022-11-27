def longest_palindromic_subsequence(s):
    def recursion(lookup_table, s, start_index, end_index):
        print("recursion called for start: {}, end: {}".format(start_index, end_index))
        
        if lookup_table[start_index][end_index] > 0:
            print("lookup_table[{}][{}] exists".format(start_index, end_index))
            return lookup_table[start_index][end_index]
        if start_index >= end_index :
            print("exit!!")
            lookup_table[start_index][end_index] = 1
            return 1
            
        updated_end_index = start_index
        for i in range(end_index, start_index, -1):
            if s[i]==s[start_index]:
                updated_end_index = i-1
                break
        print("updated_end_index: {}".format(updated_end_index))
        include_num = 2 + recursion(lookup_table, s, start_index+1, updated_end_index)
        not_include_num = recursion(lookup_table, s, start_index+1, end_index)
        # print("include_num: {},not_include_num: {}".format(include_num, not_include_num))
        
        lookup_table[start_index][updated_end_index] = max(include_num, not_include_num)
        return lookup_table[start_index][updated_end_index]
    
    lookup_table = [[0 for x in range(len(s))] for x in range(len(s))]
    return recursion(lookup_table, s, 0, len(s)-1)


s = "abdbca"
print(longest_palindromic_subsequence(s))
