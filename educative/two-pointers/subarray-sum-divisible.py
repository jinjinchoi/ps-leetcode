from typing import List
from collections import Counter
def subarray_sum_divisible(nums: List[int], K:int)->int:
	remainder_counter = Counter({0: 1})
	sum = 0
	count = 0
	for i, n in enumerate(nums):
	    sum += n
	    remainder = sum % K
	    compliment = (K-remainder)%K 
	    print("i[{}] n[{}] remainder{} compliment{}".format(i, n, remainder, compliment))
	    if compliment in remainder_counter:
	        count += remainder_counter[compliment]
	    remainder_counter[compliment] += 1
	return count
	
	
# Driver code
inputs = ["3 1 2 5 1"]
inputs1 = ["3"]
for i in range(len(inputs)):
    nums = [int(x) for x in inputs[i].split()]
    K = int(inputs1[i])
    print("Subarray sum divisible : ",subarray_sum_divisible(nums, K))  
