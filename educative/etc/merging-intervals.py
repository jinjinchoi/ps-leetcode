from typing import List
def mergeInterval(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    def overlap(interval1, interval2):
        return not(interval2[1]<interval1[0] or interval1[1]<interval2[0])
    
    res = []
    start_index =  curr_max_index = 0
    for interval in intervals:
        if not res or not overlap(res[-1], interval):
            res.append(interval)
        else:
            res[-1][1] = max(interval[1], res[-1][1])
    
    return res
    
    
    
#Driver code
inputs = [[[1, 3], [2, 6], [8, 10], [15,18]],[[1, 4], [4, 5]]]
for i in range(len(inputs)):
    print("Merge interval :",mergeInterval(inputs[i]))   
