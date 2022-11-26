from typing import List
def mergeInterval(intervals: List[List[int]]) -> bool:
    intervals.sort()
    def overlaps(interval1, interval2):
        return not(interval2[1]<interval1[0] or interval1[1]<interval2[0])
    for i in range(1, len(intervals)):
        if overlaps(intervals[i-1], intervals[i]):
            return False
    return True
    
    
#Driver code
inputs = [[[0,30],[5, 10],[15,20]],[[7,10],[2, 4]]]
for i in range(len(inputs)):
  print("Merge interval: ",mergeInterval(inputs[i]))

