def count_ways(n):
    print("count_ways called for {}".format(n))
    lookup_table = {1:1, 2:2, 3:4}
    if n in lookup_table:
        print("{} in lookup_table".format(n))
        return lookup_table[n]
    ways = count_ways(n-1)+count_ways(n-2)+count_ways(n-3)
    lookup_table[n] = ways
    return lookup_table[n]
